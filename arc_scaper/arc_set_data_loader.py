from threading import Timer
from arc_query_builder import ArcQueryBuilder
from arc_enum import ArcFormat, ArcOutStatistic, ArcStatisticType
from requests import get, Session
from helpers import json_to_wkt, exception_logging, esri_geometry_to_empty_wtk
from time import time
from json import dumps
from datetime import datetime
from tqdm import tqdm
# from shapely.validation import make_valid
# from shapely.geometry import multipolygon, point, multilinestring


class ArcSetDataLoader:

    def __init__(self, arc_set,
                 result_record_count=10,
                 max_result_record_count=100,
                 max_tries=1,
                 target_time=30000,  # milliseconds
                 timeout=30,  # seconds
                 allowable_offset = 0,
                 max_allowable_offset=1025,
                 geometry_precision=7,
                 extra_query_params={}):
        self.__arc_set = arc_set
        self.__db_client = arc_set.db_client
        self.__result_record_count = result_record_count
        self.__max_result_record_count = min(max_result_record_count, arc_set.max_record_count)
        self.__max_tries = max_tries
        self.__target_time = target_time
        self.__errors = list()
        self.__result_offset = 0
        self.__timer = self.init_timer()
        self.__OIDs = set()
        self.__loaded_OIDs = set()
        self.__OIDs_to_load = set()
        self.__min_OID = 0
        self.__max_OID = 0
        self.__object_id_field_name = "FID"
        self.__record_count = 0
        self.__result_offset = 0
        self.__timeout = timeout
        self.__tries = 0
        self.__loaded_record_count = 0
        self.__millis = 0
        self.__t0 = 0
        self.__http_success_record_no = {}
        self.__error_persist = arc_set.db_error_logger
        self.__get = Session().get
        self.__pbar = None
        self.__extra_query_params = extra_query_params
        self.__allowable_offset = allowable_offset
        self.__max_allowable_offset = max_allowable_offset
        self.__geometry_precision = geometry_precision
    # __sql_generator_templates = {
    #     "insert_stats": "INSERT INTO TableStats(TableName, MinOID, MaxOID, RecordCount, LoadedRecordCount) \
    #     VALUES('{table_name}',{min_OID},{max_OID},{record_count},{loaded_record_count}}"
    # }

    #     List<int> OIDsToLoad;
    def init_timer(self):
        return Timer(.0001, self.__increment_millis)

    def __increment_millis(self):
        """
        increments millis variable, called by timer every millisecond
        :return: None
        """
        self.__millis += 1

    def __stop_timer(self):
        """
        stops the timer and resets the counter variable before returning the number of milliseconds since the timer
        was started
        :return: milliseconds since the timer was started
        """
        self.__timer.cancel()
        millis = self.__millis
        self.__millis = 0
        return millis

    @property
    def object_id_field_name(self):
        return self.__object_id_field_name

    @property
    def errors(self):
        return self.__errors
    
    def __add_error(self, e):
        self.__errors.append(e)
        exception_logging(e, self.__error_persist)
        
    @property
    def arc_set(self):
        return self.__arc_set

    @arc_set.setter
    def arc_set(self, value):
        self.__arc_set = value

    @property
    def db_client(self):
        return self.__db_client

    @db_client.setter
    def db_client(self, value):
        self.__db_client = value

    @property
    def result_record_count(self):
        return self.__result_record_count

    @result_record_count.setter
    def result_record_count(self, value):
        self.__result_record_count = value

    @property
    def max_result_record_count(self):
        return self.__max_result_record_count

    @max_result_record_count.setter
    def max_result_record_count(self, value):
        self.__max_result_record_count = min(value, self.arc_set.max_record_count)

    @property
    def max_tries(self):
        return self.__max_tries

    @max_tries.setter
    def max_tries(self, value):
        self.__max_tries = value

    @property
    def target_time(self):
        return self.__target_time

    @target_time.setter
    def target_time(self, value):
        self.__target_time = value

    @property
    def result_offset(self):
        return self.__result_offset

    @result_offset.setter
    def result_offset(self, value):
        self.__result_offset = value

    @property
    def loaded_record_count(self):
        return self.__loaded_record_count

    @property
    def record_count(self):
        return self.__record_count

    def load_stats(self):
        try:
            query_builder = ArcQueryBuilder(self.__arc_set)
            query_builder.where = "1=1"
            query_builder.format = ArcFormat.JSON.value
            query_builder.return_ids_only = True

            # try to load object ids

            if not self.__try_get_object_ids(query_builder):
                # try to load stats
                query_builder.return_ids_only = False

                if bool((self.arc_set.advanced_query_capabilities).get("supportsStatistics", False)):
                    arc_stat_min = ArcOutStatistic(ArcStatisticType.MIN, self.__object_id_field_name, "MinOID")
                    arc_stat_max = ArcOutStatistic(ArcStatisticType.MAX, self.__object_id_field_name, "MaxOID")
                    arc_stat_cnt = ArcOutStatistic(ArcStatisticType.COUNT, self.__object_id_field_name, "Count")
                    query_builder.out_statistics = [arc_stat_min, arc_stat_max, arc_stat_cnt]
                    if not self.__try_get_stats(query_builder):
                        query_builder.out_statistics = None
                        query_builder.result_record_count = True
                        if not self.__try_get_record_count(query_builder):
                            raise Exception("Can not load statistics")

                else:
                    query_builder.result_record_count = True
                    if not self.__try_get_record_count(query_builder):
                        raise Exception("Can not load statistics")

            # get loaded object ids from database
            self.__get_object_ids_from_db()

            return True
        except Exception as e:
            self.__add_error(e)
            return False

    def __try_get_record_count(self, query):
        response = self.__get(query)
        if response.ok and "error" not in response.json():
            json = response.json()
            self.__record_count = int(json['Count'])
            self.__pbar = tqdm(total=self.__record_count)
            return True
        else:
            return False

    def __try_get_stats(self, query):
        response = self.__get(query)
        if response.ok and "error" not in response.json():
            json = response.json()
            feat = json['feature'][0]
            att = feat['attributes']
            self.__max_OID = int(att['MaxOID'])
            self.__min_OID = int(att['MinOID'])
            self.__record_count = int(att['Count'])
            self.__pbar = tqdm(total=self.__record_count)
            return True
        else:
            return False

    def __try_get_object_ids(self, query):
        response = self.__get(query)
        if response.ok and "error" not in response.json():
            json = response.json()
            self.__OIDs = set(json.get('objectIds', set()))
            self.__min_OID = min(self.__OIDs)
            self.__max_OID = max(self.__OIDs)
            self.__record_count = len(self.__OIDs)
            self.__pbar = tqdm(total=self.__record_count)
            self.__object_id_field_name = json['objectIdFieldName']
            return True
        else:
            return False

    def load_data(self):
        try:
            # TODO: surface out_SR and geo precision as parameter
            # TODO: add support for true curves
            paged = self.__arc_set.advanced_query_capabilities.get("supportsPagination", False)
            print(f"start loading {self.arc_set.name}({self.arc_set.sql_full_table_name})")
            if self.load_stats():
                #print(f"loaded stats for {self.arc_set.name}")
                self.__tries = 0
                query_builder = ArcQueryBuilder(self.arc_set)
                query_builder.where = "1=1"
                query_builder.out_fields = self.arc_set.fields
                query_builder.format = ArcFormat.JSON.value
                query_builder.return_true_curves = False
                query_builder.out_SR = self.arc_set.SR_id
                query_builder.geometry_precision = self.__geometry_precision
                for k, v in self.__extra_query_params:
                    setattr(query_builder, k, v)

                self.__OIDs_to_load = list(self.__OIDs - self.__loaded_OIDs)
                self.__pbar.update(self.__loaded_record_count)
                if self.__loaded_record_count == self.__record_count:
                    # print(f"Finished loading {self.__loaded_record_count} of {self.__record_count} for table {self.arc_set.name}.")
                    return

                if len(self.__OIDs_to_load):  # load by record id
                    while self.__result_offset < len(self.__OIDs_to_load):
                        start = self.__result_offset
                        end = self.__result_offset + self.__result_record_count
                        query_builder.object_ids = self.__OIDs_to_load[start: end]
                        self.__load_batch(query_builder)

                elif paged:
                    while self.__result_offset < self.__record_count:
                        query_builder.result_record_count = self.__result_record_count
                        query_builder.result_offset = self.__result_offset
                        self.__load_batch(query_builder)
                        self.__result_offset += self.__result_record_count

                elif self.__max_OID > 0:
                    while self.__result_offset < self.__max_OID:
                        query_builder.where = "{0}>={1} and {0}<{2}".format(self.__object_id_field_name,
                                                                            self.result_offset,
                                                                            self.result_offset +
                                                                            self.__result_record_count)
                        self.__load_batch(query_builder)

                else:  # load by record count
                    while self.__result_offset < self.__record_count:
                        query_builder.where = "{0}>={1} and {0}<{2}".format(self.__object_id_field_name,
                                                                            self.result_offset,
                                                                            self.result_offset +
                                                                            self.__result_record_count)
                        self.__load_batch(query_builder)
            else:
                if self.__tries < self.__max_tries:
                    self.__tries += 1
                    print(f"Trying to loading {self.arc_set.name}  for the {self.__tries}!")
                    self.load_data()
                else:
                    self.errors.append(Exception("Can not load metadata for {}".format(self.arc_set.name)))

        except Exception as e:
            self.__add_error(e)
            print(f"finished loading {self.arc_set.name} with error!")
        finally:
            self.save_stats_to_db()
            if self.__pbar is not None:
                self.__pbar.close()
            print(f"Finished loading {self.__loaded_record_count} of {self.__record_count} with {len(self.errors)} errors for table {self.arc_set.name} ({self.arc_set.sql_full_table_name}).\n ")
            for e in self.errors:
                print(e)

    def __load_batch(self, query):
        query_result = self.try_load_records(query)
        if query_result:
            self.__tries = 0
            # print(f"Successfully tried to downloaded {len(query_result.get('features',[]))}  records for  {self.arc_set.name} !")
            rows_inserted = self.parse_and_save_json_data(query_result)
            if rows_inserted:
                return rows_inserted
            else:
                self.errors.append(Exception("Cannot parse and save records for {}".format(query)))
        else:
            self.errors.append(Exception("Cannot fetch query for {}".format(query)))

    def try_load_records(self, query_builder):

        try:
            # self.__timer = self.init_timer()
            # self.__timer.start()
            self.__t0 = time()
            response = self.__get(query_builder, timeout=self.__timeout)
            if response.ok and "error" not in response.json():

                self.__result_offset += self.__result_record_count
                # millis = self.__stop_timer()
                elapsed = time()-self.__t0
                # learning the optimal number of records to try and download

                millis_per_record = (elapsed*1000)/self.__result_record_count

                self.__http_success_record_no[self.__result_record_count] = 1/millis_per_record

                opt_record_no = min([int(self.__target_time/millis_per_record), self.max_result_record_count])

                self.__result_record_count = max(1, min(self.max_result_record_count, int((sum([k*float(v) for k, v in self.__http_success_record_no.items()])
                                                 + (opt_record_no*(1/self.__target_time))) /
                                                 (sum([v for k, v in self.__http_success_record_no.items()]) + 1/millis_per_record))))
                self.__target_time = min(self.__target_time * 1.1, 30000)

                query_builder.max_allowable_offset = self.__allowable_offset

                return response.json()
            elif "error" in response.json():
                elapsed = time() - self.__t0
                self.__target_time = min(elapsed * 1000 * .75, self.__target_time, 30000)
                raise Exception(response.text)
            else:
                raise Exception(response.text)
        except Exception as e:
            try:
                # self.__stop_timer()
                # print(f"Try downloaded {self.__result_record_count} records for  {self.arc_set.name}  for the {self.__tries} time!")
                self.__add_error(Exception("Error on try_load_records for query {0}, message:{1}"
                                           .format(query_builder, e)))
                if self.__result_record_count > 1:
                    self.__result_record_count = max(1, int(self.__result_record_count * .3))
                    # self.try_load_records(query_builder)
                elif self.__tries < self.__max_tries:

                    self.__tries += 1
                    # self.try_load_records(query_builder)
                elif query_builder.max_allowable_offset < self.__max_allowable_offset:
                    new_offset = min(max(query_builder.max_allowable_offset**2, 2), self.__max_allowable_offset)
                    query_builder.max_allowable_offset = new_offset
                else:
                    self.__tries = 0
                    query_builder.max_allowable_offset = self.__allowable_offset
                    self.__result_offset += self.__result_record_count
                return False
            except Exception as e:
                self.__add_error(e)
                return False

    def parse_and_save_json_data(self, json):
        try:
            if json:
                geom_col_name = [self.__db_client.sanitize_and_quote_name(f['name']) for f in self.arc_set.fields
                                 if f['type'] == "esriFieldTypeGeometry"]
                geometry_type = self.arc_set.geometry_type
                col_names = geom_col_name.copy()
                if 'fields' in json:
                    col_names += [self.__db_client.sanitize_and_quote_name(n['name']) for n in (json.get('fields', {}))]
                else:
                    col_names += [self.__db_client.sanitize_and_quote_name(k) for k, v
                                  in json.get('feature', {'attributes': {}}).get('attributes', {}).items()]

                inserts = list()
                data_row_insert = self.__db_client.sql_generator_templates["data_row_insert"]
                spatial_data_insert = self.__db_client.sql_generator_templates["spatial_data_insert"]
                # null_spatial_data_insert = self.__db_client.sql_generator_templates["null_spatial_data_insert"]

                def formatter(row):
                    return f"{row}"

                p = {
                    'table_name': self.arc_set.sql_full_table_name,
                    'columns': ",".join(col_names),
                    'values': '{0}'
                }
                insert_template = self.__db_client.sql_generator_templates['data_insert'].format(**p)

                def non_geom(json):
                    return esri_geometry_to_empty_wtk.get(geometry_type, 'POINT EMPTY')

                for f in (json.get('features', []) or [json.get('feature', None)]):

                    values = ",".join(["'{}' ".format(str(v).replace("'", "''")) if str(v).strip() != '' and v is not None
                                       else "NULL " for k, v in f['attributes'].items()])

                    if geometry_type and len(geom_col_name)>0:
                        geom = f.get('geometry', '')
                        wkt = json_to_wkt.get(geometry_type, non_geom)(geom)
                        # TODO: when next version of pygeos or shapely comes out add make_valid to fix any invalid geometries.

                        if wkt.strip() in ["", "()"]:
                            wkt = non_geom('')   # ensure that wkt is not null
                        #    inserts.append(null_spatial_data_insert.format(values=values))
                        # else:
                        inserts.append(spatial_data_insert.format(values=values, wkt=wkt))
                    else:
                        inserts.append(data_row_insert.format(values=values))

                k = self.__db_client.run_bulk_insert(insert_template, inserts, formatter, batch=1000)
                self.__loaded_record_count += k
                if self.__pbar is not None:
                    self.__pbar.update(k)
                # print(f"loaded {self.__loaded_record_count} of {self.__record_count} into {self.arc_set.name}")
                return k
            else:
                raise Exception("empty json")
                return 0
        except Exception as e:
            self.__add_error(e)
            return 0

    def save_stats_to_db(self):
        try:
            p = {
                'table_name': self.arc_set.sql_full_table_name,
                'timestamp': self.__db_client.string_date(datetime.now()),
                'min_OID': self.__min_OID,
                'max_OID': self.__max_OID,
                'record_count': self.__record_count,
                'loaded_record_count': self.__loaded_record_count,
                'url': self.__db_client.insert_safe(self.arc_set.uri),
                'json': self.__db_client.insert_safe(dumps(self.arc_set.raw_json)),
                'errors': 'NULL' if len(self.errors) == 0
                else "'{}'".format((",".join([self.__db_client.insert_safe(str(e)) for e in self.errors]))[:512])
            }
            sql_stm = self.__db_client.sql_generator_templates['insert_stats'].format(**p)
            self.__db_client.exec_non_query(sql_stm)
            return True
        except Exception as e:
            self.__add_error(e)
            return False

    def __get_object_ids_from_db(self):
        try:
            p = {
                'table_name': self.__arc_set.sql_full_table_name,
                'object_id_field_name': self.__object_id_field_name
            }
            sql = self.__db_client.sql_generator_templates['select_object_ids'].format(**p)
            results = self.__db_client.exec_result_set_query(sql) or {}
            self.__loaded_OIDs = {r[0] for r in results}
            self.__loaded_record_count = len(self.__loaded_OIDs)
            return self.__loaded_OIDs
        except Exception as e:
            self.__add_error(e)
