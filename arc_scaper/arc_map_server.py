from arc_base import ArcBase
# from arc_service import ArcService
from arc_layer import ArcLayer
from arc_table import ArcTable
from itertools import product


class ArcMapServer(ArcBase):

    def __init__(self, uri, folder, arc_service, db_client):
        """

        :param uri:
        :param folder:
        :param arc_service:
        :param db_client:
        """
        super().__init__(uri, db_client)
        # if not isinstance(arc_service, ArcService):
        #     raise Exception("arc service must be of type ArcService")
        self._arc_service = arc_service
        self._folder = folder  # schema name
        self._tables = list()
        self._layers = list()
        self.load_meta_data()

    # _sql_generator_templates = {
    #     "foreign_key_constraint": "ALTER TABLE [{schema}].[{table_name}]\nADD CONSTRAINT [fk_{name}] \
    #     FOREIGN KEY({column}) REFERENCES [{ref_schema}].[{re_table_name}] ([{ref_column}])\nGO"
    # }

    @property
    def errors(self):
        return [e for t in self.tables for e in t.errors] + [e for l in self.layers for e in l.errors]\
               + self._errors

    @property
    def service_description(self):
        return self.raw_json.get('serviceDescription', None)

    @property
    def map_name(self):
        return self.raw_json.get('mapName', None)

    @property
    def folder(self):
        return self.raw_json.get('folder', None)

    @property
    def description(self):
        return self.raw_json.get('description', None)

    @property
    def copyright_text(self):
        return self.raw_json.get('copyrightText', None)
#     public string CopyrightText { get; set; }

    @property
    def supports_dynamic_layers(self):
        return self.raw_json.get('supportsDynamicLayers', False)

    @property
    def tables(self):
        return self._tables

    @property
    def layers(self):
        return self._layers

    @property
    def json_layers(self):
        return self.raw_json.get('layers', [])

    @property
    def json_tables(self):
        return self.raw_json.get('tables', [])

    def _generate_relationship_sql(self, rel_scr, rel_dst):

        p = {
            "schema": self.db_client.sanitize_and_quote_name(rel_dst['folder'], self.db_client.quote_characters),
            "table_name": self.db_client.sanitize_and_quote_name(rel_dst['set'], self.db_client.quote_characters),
            "name": self.db_client.sanitize_name(rel_dst['name']),
            "column": self.db_client.sanitize_name(rel_dst['keyField']),
            "ref_schema": self.db_client.sanitize_and_quote_name(rel_scr['folder'], self.db_client.quote_characters),
            "ref_table_name": self.db_client.sanitize_and_quote_name(rel_scr['set'], self.db_client.quote_characters),
            "ref_column": self.db_client.sanitize_name(rel_scr['keyField']),
        }
        return self.db_client.sql_generator_templates["foreign_key_constraint"].format(**p)

    def generate_sql(self):
        try:
            sql = self.db_client.statement_terminator.join([t.generate_sql() for t in self._tables
                                                            if bool(t.generate_sql()
                                                                    .replace(self.db_client.statement_terminator, "")
                                                                    .strip())]
                                                           + [l.generate_sql() for l in self._layers
                                                              if bool(l.generate_sql()
                                                                      .replace(self.db_client.statement_terminator, "")
                                                                      .strip())])
            return sql.strip()
        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_extra(self):
        """
        [{'id': 0, 'name': 'dbklhk.pkps_pskl.kemitraan_hut', 'relatedTableId': 1, 'role': 'esriRelRoleOrigin', 'keyField': 'id_usulan_iphps', 'cardinality': 'esriRelCardinalityOneToOne', 'composite': False}]
        [{'id': 0, 'name': 'dbklhk.pkps_pskl.usulan_iphps', 'relatedTableId': 0, 'role': 'esriRelRoleDestination', 'keyField': 'id_usulan_kk', 'cardinality': 'esriRelCardinalityOneToOne', 'composite': False}]
        :return:
        """
        try:

            if any([bool(r['composite']) for t in self.tables for r in t.relationships]
                   + [bool(r['composite']) for t in self.layers for r in t.relationships]):
                self._errors.append(Exception("Composite relationships not implemented"))
            sql = ""
            if self._db_client.sql_generator_options['enforce_relationships']:
                relsrc = [{**r, **{'setId': tab.id, 'set': tab.name, 'folder': tab.folder}}
                          for tab in self._tables for r in tab.relationships
                          if r['role'] == "esriRelRoleOrigin" and not bool(r['composite'])] +\
                         [{**r, **{'setId': lay.id, 'set': lay.name, 'folder': lay.folder}}
                          for lay in self._layers for r in lay.relationships
                          if r['role'] == "esriRelRoleOrigin" and not bool(r['composite'])]

                reldst = [{**r, **{'setId': tab.id, 'set': tab.name, 'folder': tab.folder}}
                          for tab in self._tables for r in tab.relationships
                          if r['role'] == "esriRelRoleDestination" and not bool(r['composite'])] +\
                         [{**r, **{'setId': lay.id, 'set': lay.name, 'folder': lay.folder}}
                          for lay in self._layers for r in lay.relationships
                          if r['role'] == "esriRelRoleDestination" and not bool(r['composite'])]

                rel = "\n".join([self._generate_relationship_sql(s, d) for s, d in product(relsrc, reldst)
                                if s['id'] == d['id']
                                and s['relatedTableId'] == d['setId']
                                and d['relatedTableId'] == s['setId']])
                sql = "{0}\n{1}".format("\n".join([x.generate_sql_extra() for x in self._tables] +
                                                  [x.generate_sql_extra() for x in self._layers]), rel)
            if sql.replace(self.db_client.statement_terminator, '').strip() == "":
                return ""
            else:
                return sql.strip()

        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_preamble(self):
        sql = self.db_client.statement_terminator.join([l.generate_sql_preamble().strip() for l in self.layers
                                                        if bool(l.generate_sql_preamble().strip()
                                                                .replace(self.db_client.statement_terminator, ""))]
                                                       + [t.generate_sql_preamble().strip() for t in self.tables
                                                          if bool(t.generate_sql_preamble().strip()
                                                                  .replace(self.db_client.statement_terminator, ""))])
        if sql.replace(self.db_client.statement_terminator, '').strip() == "":
            return ""
        else:
            return sql.strip()

    def load_meta_data(self):
        try:
            self.load_json()
            self._layers = [ArcLayer("{0}/{1}".format(self.uri, l['id']),
                                     self._folder,
                                     self.db_client) for l in self.json_layers]

            self._tables = [ArcTable("{0}/{1}".format(self.uri, l['id']),
                                     self._folder,
                                     self.db_client) for l in self.json_tables]

            # convert to async
            # for l in self.layers:
            #     l.load_meta_data()
            # for t in self.tables:
            #     t.load_meta_data()

            # await loading
            self.loaded = all([t.loaded for t in self._tables] + [l.loaded for l in self._layers])
        except Exception as e:
            self.add_error(e)
            self.loaded = False
        finally:
            return self.loaded
