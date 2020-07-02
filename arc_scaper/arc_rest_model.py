from arc_base import ArcBase
import arc_service
from urllib.parse import urlparse
from helpers import validate_url
from warnings import warn
from arc_set_data_loader import ArcSetDataLoader


class ArcRestModel(ArcBase):

    def __init__(self, uri, database, db_client):
        """

        :param uri:
        :param db_client:
        """
        super().__init__(uri, db_client)
        self._database = database
        self._arc_services = list()
        self.load_meta_data()


    # _sql_generator_templates = {'create_database': "IF DB_ID('{database}') IS NULL CREATE DATABASE \
    # [{database}]\nGO\nUSE [{database}]\nGO\n{sql_stm}"}

    @property
    def arc_services(self):
        return self._arc_services

    @property
    def errors(self):

        return [e for a_s in self.arc_services for e in a_s.errors] + self._errors

    @property
    def version(self):
        return self.raw_json.get('version', None)

    @property
    def folders(self):
        return self.raw_json.get('folders', [])

    def generate_sql(self):
        """

        :return:
        """
        try:

            sql_stm = self.db_client.statement_terminator.join([s.generate_sql().strip() for s in self._arc_services
                                 if bool(s.generate_sql().replace(self.db_client.statement_terminator, "").strip())])
            p = {'database': self._database}
            sql = self.db_client.sql_generator_templates['create_database'].format(**p)
            sql += self.db_client.statement_terminator if bool(sql) else "" + self.db_client.sql_generator_templates['create_stats_table']
            sql += self.db_client.statement_terminator + self.generate_sql_preamble()
            sql += self.db_client.statement_terminator + sql_stm
            return sql
        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_extra(self):
        """

        :return:
        """
        try:
            sql = self.db_client.statement_terminator.join([s.generate_sql_extra() for s in self.arc_services
                                                            if bool(s.generate_sql()
                                                                    .replace(self.db_client.statement_terminator, "")
                                                                    .strip())])
            if sql.replace(self.db_client.statement_terminator, '').strip() == "":
                return ""
            else:
                return sql.strip() + self.db_client.statement_terminator
        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_preamble(self):
        sql = self.db_client.statement_terminator.join([l.generate_sql_preamble().strip() for l in self.arc_services
                                                        if bool(l.generate_sql_preamble()
                                                                .replace(self.db_client.statement_terminator, "")
                                                                .strip())])
        if sql.replace(self.db_client.statement_terminator, '').strip() == "":
            return ""
        else:
            return sql.strip() + self.db_client.statement_terminator

    def save_sql_script(self, path):
        """

        :param path:
        :return:
        """
        sql = self.generate_sql() + self.generate_sql_extra()
        with open(path, 'w+') as f:
            f.write(sql)

    def run_sql(self, db_master='master'):
        """

        :param sep:
        :param db_master:
        :return:
        """

        if self.db_client.db_conn.get('database', '') == db_master:
            database = urlparse(self.uri).netloc.replace(".", "_")
        else:
            database = self.db_client.db_conn['database']

        self.db_client.db_conn['database'] = db_master

        try:
            sql = self.generate_sql() + self.generate_sql_extra()
            sql_stm = sql.split(sep=self.db_client.statement_terminator.strip())

            self.db_client.exec_non_query(sql_stm[1], autocommit=True)

            self.db_client.db_conn['database'] = database
            self.db_client.exec_non_query(sql_stm[3:], autocommit=True)

        except Exception as e:
            self.add_error(e)
            raise e

    def add_arc_service(self, service):

        if not isinstance(service, arc_service.ArcService):
            raise Exception("service parameter must be of type ArcService")
        self._arc_services.append(service)

    def remove_arc_service(self, service):
        if not isinstance(service, arc_service.ArcService):
            raise Exception("service parameter must be of type ArcService")
        self._arc_services.remove(service)

    def add_arc_service_from_uri(self, uri):
        if not validate_url(uri):
            raise Exception("Uri for arc service is not valid")
        name = uri.split("/")[-1]
        arc_s = arc_service.ArcService(uri, name, self, self.db_client)
        self.add_arc_service(arc_s)

    def remove_arc_service_from_uri(self, uri):
        if not validate_url(uri):
            raise Exception("Uri for arc service is not valid")
        arc_s = ([s for s in self.arc_services if s.uri == uri] + [None])[0]
        if arc_s is not None:
            self.remove_arc_service(arc_s)

    def load_meta_data(self):
        try:
            self.load_json()

            for f in self.folders:
                uri = "{0}/services/{1}".format(self.uri, f)
                arc_s = arc_service.ArcService(uri, f, self, self.db_client)
                # arc_s.load_meta_data()
                self.add_arc_service(arc_s)
                if not arc_s.loaded:
                    self._errors.append(Exception("Can't load {}".format(uri)))

            self.loaded = all([s.loaded for s in self.arc_services])

        except Exception as e:
            self.loaded = False
            self.add_error(e)
        finally:
            if len(self._errors) > 0:
                warn("Error have occurred, check the errors list for details")
            return self.loaded

    # TODO: add concurrency with asyncro
    def load_data(self, **kargs):  # int concurrency=5, int resultRecordCount=10, int maxResultRecordCount=100)
        try:
            layers = [l for s in self._arc_services for m in s.arc_map_servers for l in m.layers if l.loaded]
            for l in layers:
                loader = ArcSetDataLoader(l, self.db_client, **kargs)
                loader.load_data()

            layers = [l for s in self._arc_services for m in s.arc_map_servers for l in m.tables]
            for l in layers:
                loader = ArcSetDataLoader(l, self.db_client, **kargs)
                loader.load_data()

        except Exception as e:
            self.add_error(e)
