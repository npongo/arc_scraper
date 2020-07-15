from arc_base import ArcBase
from arc_map_server import ArcMapServer
from helpers import validate_url
from warnings import warn


class ArcService(ArcBase):

    def __init__(self, uri, name, rest_model, db_client, SR_id=4326):
        """

        :param uri:
        :param name:
        :param rest_model:
        :param db_client:
        """
        super().__init__(uri, db_client, SR_id=SR_id)
        # if not isinstance(rest_model, ArcRestModel):
        #     raise Exception("rest model must be of type ArcRestModel")
        self._arc_map_servers = list()
        self._arc_rest_model = rest_model
        self._name = name
        self.load_meta_data()

    # _sql_generator_templates = {
    #     "create_schema": "INSERT INTO TableStats(TableName, MinOID, MaxOID, RecordCount, LoadedRecordCount) \
    #      VALUES('{table_name}',{min_OID},{max_OID},{record_count},{loaded_record_count}}",
    #     "create_schema": "IF SCHEMA_ID('{schema}') IS NULL EXEC('CREATE SCHEMA[{schema}]')\nGO"
    # }

    @property
    def SR_id(self):
        return self._SR_id

    @property
    def arc_rest_model(self):
        return self._arc_rest_model

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def services(self):
        return self.raw_json.get('services', [])

    @property
    def errors(self):
        return [e for ams in self._arc_map_servers for e in ams.errors] + self._errors

    @property
    def arc_map_servers(self):
        return self._arc_map_servers

    def add_arc_map_server(self, map_server):
        if not isinstance(map_server, ArcMapServer):
            raise Exception("map_server is not of the correct type ArcMap: {type(map_server_}")
        self._arc_map_servers.append(map_server)

    def remove_arc_map_server(self, map_server):
        self._arc_map_servers.remove(map_server)

    def add_arc_map_server_from_uri(self, uri, folder):
        ams = ArcMapServer(uri, folder, self, self._db_client)
        self.remove_arc_map_server(ams)

    def remove_arc_map_service_from_uri(self, uri):
        if validate_url(uri):
            ams = ([a for a in self._arc_map_servers if a.uri == uri] + [None])[0]
            if ams is not None:
                self.remove_arc_map_server(ams)
        else:
            warn("not a valid Url: {}".format(uri))

    def _generate_schema(self):
        if len([l for ms in self._arc_map_servers for l in ms.layers]) + \
           len([l for ms in self._arc_map_servers for l in ms.tables]) == 0:
            return ""

        p = {
            'schema': self.db_client.sanitize_name(self.name),
            'schema_quoted': self.db_client.sanitize_and_quote_name(self.name)
        }
        sql = self.db_client.sql_generator_templates['create_schema'].\
            format(**p)
        return sql

    def generate_sql(self):
        try:
            sql = self.db_client.statement_terminator.join([a.generate_sql().strip() for a in self.arc_map_servers
                                                            if bool(a.generate_sql()
                                                                    .replace(self.db_client.statement_terminator, "")
                                                                    .strip())])
            return sql
        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_extra(self):
        try:
            sql = self.db_client.statement_terminator.join([a.generate_sql_extra().strip() for a in self.arc_map_servers
                                                            if bool(a.generate_sql_extra()
                                                                    .replace(self.db_client.statement_terminator, "")
                                                                    .strip())])
            if sql.replace(self.db_client.statement_terminator, '').strip() == "":
                return ""
            else:
                return sql
        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_preamble(self):
        schema = self._generate_schema().strip()
        sql = self.db_client.statement_terminator.join([l.generate_sql_preamble() for l in self.arc_map_servers
                                                        if bool(l.generate_sql_preamble().strip()
                                                                .replace(self.db_client.statement_terminator, ""))])
        if sql.replace(self.db_client.statement_terminator, '').strip() == "":
            return schema.strip()
        else:
            return schema.strip() + self.db_client.statement_terminator + sql

    def load_meta_data(self):
        try:
            self.load_json()
            for s in [s for s in self.services if s['type'] == 'MapServer']:
                name = self.name
                uri = f"{self.uri}/{s['name'].split('/')[-1]}/MapServer"
                ams = ArcMapServer(uri, name, self, self.db_client, SR_id=self._SR_id)
                self._arc_map_servers.append(ams)
                # ams.load_meta_data()

            for f in self.raw_json.get('folders', []):
                uri_list = list(self.uri.partition("?"))
                uri_list.insert(1, f"/{f}")
                uri = "".join(uri_list)
                arc_service = ArcService(uri, f"{self.name}_{f}",
                                         self._arc_rest_model,
                                         self.db_client,
                                         SR_id=self._SR_id)
                arc_service.load_meta_data()
                # self._arc_rest_model.add_arc_service(arc_service)

            self.loaded = all([m.loaded for m in self._arc_map_servers])
        except Exception as e:
            self.add_error(e)
            self.loaded = False
        finally:
            return self.loaded
