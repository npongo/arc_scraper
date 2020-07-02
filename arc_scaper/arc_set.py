from arc_scaper.arc_base import ArcBase
from itertools import product

class ArcSet(ArcBase):

    def __init__(self, uri, folder, db_client):
        super().__init__(uri, db_client)
        assert isinstance(folder, str)
        self._folder = folder

    # _sql_generator_templates = {
    #     "table_name": "[{schema}].[{table_name}]",
    #     "null_string": "NULL",
    #     "esriFieldTypeOID": "[{name}] {type} NOT NULL",
    #     "esriFieldTypeString": "[{name}] {type}({length}) {null}",
    #     "esriFieldTypeDate": "[{name}] {type} {null}: \n[{name}_Date] AS (dateadd(millisecond: [{name}]%(60000):\
    #      dateadd(minute: [{name}]/(60000): '1970-01-01 00:00:00.000')))",
    #     "unique_field": "NOT NULL UNIQUE",
    #     "unique_constraint": "CONSTRAINT [{folder}_{name}_{idx_name}] UNIQUE([{idx_fields}])",
    #     "primary_key": "CONSTRAINT [pk_{folder}_{name}_{idx_name}] PRIMARY KEY([{idx_fields}])",
    #     "create_spatial_index": "CREATE SPATIAL INDEX [spidx_{folder}_{idx_name}_{idx_fields}] ON [{folder}]. \
    #     [{idx_name}]({idx_fields}) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = {xmin}:  ymin = {ymin}: \
    #      xmax = {xmax}:  ymax = {ymax})); ",
    #     "create_index": "CREATE INDEX [{folder}_{name}_{idx_name}] ON [{folder}].[{name}]({idx_fields})",
    #     "drop_if_exists_create_table": "IF OBJECT_ID('{table_name}') IS NOT NULL\n\t \
    #     DROP TABLE {table_name}\nGO\nCREATE TABLE {table_name} (\n{fields}{constraints}\n)\nGO\n",
    #     "rangeValue": "CONSTRAINT CK_{field}_range_domain CHECK {field} BETWEEN {min_value} AND {max_value}",
    #     "codedValue": "CONSTRAINT CK_{field}_code_domain CHECK {field} IN({value})"
    # }

    @property
    def id(self):
        return self.raw_json.get("id", None)

    @property
    def name(self):
        return self.raw_json.get("name", None)

    @property
    def folder(self):
        return self._folder

    @property
    def type(self):
        return self.raw_json.get("type", None)

    @property
    def description(self):
        return self.raw_json.get("description", None)

    @property
    def geometry_type(self):
        return self.raw_json.get("geometryType", None)

    @property
    def copyright_text(self):
        return self.raw_json.get("copyrightText", None)

    @property
    def parent_layer(self):
        return self.raw_json.get("parentLayer", None)

    @property
    def min_scale(self):
        return self.raw_json.get("minScale", None)

    @property
    def max_scale(self):
        return self.raw_json.get("maxScale", None)

    @property
    def sub_layers(self):
        return self.raw_json.get("subLayers", []) or []

    @property
    def default_visibility(self):
        return self.raw_json.get("defaultVisibility", False)

    # xmin: ymin: xmax: ymax
    @property
    def extent(self):
        return self.raw_json.get("extent", {}) or {}

    @property
    def has_attachments(self):
        return self.raw_json.get("hasAttachments", False)

    @property
    def display_field(self):
        return self.raw_json.get("displayField", None)

    @property
    def fields(self):
        return self.raw_json.get("fields", []) or []

    @property
    def domains(self):
        return [{'fieldType': f['type'], 'fieldName': f['name'], **f['domain']} for f in self.fields
                if f.get('domain', None) is not None]

    @property
    def indexes(self):
        return self.raw_json.get("indexes", []) or []

    @property
    def relationships(self):
        return self.raw_json.get("relationships", []) or []

    @property
    def can_modify_layer(self):
        return self.raw_json.get("canModifyLayer", False)

    @property
    def can_scale_symbols(self):
        return self.raw_json.get("canScaleSymbols", False)

    @property
    def capabilities(self):
        return self.raw_json.get("capabilities", []) or []

    @property
    def max_record_count(self):
        return self.raw_json.get("maxRecordCount", None)

    @property
    def supports_statistics(self):
        return self.raw_json.get("supportsStatistics", False)

    @property
    def supports_advanced_queries(self):
        return self.raw_json.get("supportsAdvancedQueries", False)

    @property
    def supported_query_formats(self):
        return self.raw_json.get("supportedQueryFormats", []) or []

    @property
    def ownership_based_access_control_for_features(self):
        return self.raw_json.get("ownershipBasedAccessControlForFeatures", {}) or []

    @property
    def use_standardized_queries(self):
        return self.raw_json.get("useStandardizedQueries", False)

    @property
    def advanced_query_capabilities(self):
        return self.raw_json.get("advancedQueryCapabilities", {}) or {}

    @property
    def sql_table_name(self):
        return "{0}.{1}".format(self.db_client.sanitize_and_quote_name(self._folder),
                                self.db_client.sanitize_and_quote_name(self.name))

    def __get_field_length(self, field):
        length = int(field['length'] * 1.25) if 'length' in field else 0
        if field.get('domain', None) is not None:
            domain = field['domain']
            length = max([len(c['code']) for c in domain.get('codedValues', [64])])
        return length

    # "<esriRelCardinalityOneToOne>|<esriRelCardinalityOneToMany>|<esriRelCardinalityManyToMany>";: //Added at 10.1
    def _generate_field_sql(self, field):
        """

        :param self:
        :param field:
        :return:
        """
        isnull = self._db_client.sql_generator_templates['null_string']

        if self._db_client.sql_generator_options['enforce_relationships']:
            for r in self.relationships:  # list of dict
                if r['keyField'] == field['name']:
                    if (r['role'] == "esriRelRoleOrigin"
                        and r['cardinality'] == "esriRelCardinalityOneToMany") \
                            or r['cardinality'] == "esriRelCardinalityOneToOne":
                        isnull = self.db_client.sql_generator_templates['unique_field']

        t = field['type']
        n = self.db_client.sanitize_and_quote_name(field['name'])
        if t == 'esriFieldTypeDate':
            n = self.db_client.sanitize_name(field['name'])
        if t == 'esriFieldTypeGeometry':  # and self.db_client.name == 'mysql':
            isnull = 'NOT NULL'

        sql_t = self.db_client.esri_types_to_sql[t]
        ff = f"{n} {sql_t} {isnull}"

        if t in self.db_client.sql_generator_templates:
            p = {'name': n,
                 'type': sql_t,
                 'length': self.__get_field_length(field),
                 'null': isnull
                 }
            ff = self.db_client.sql_generator_templates[t].format(**p)

        return ff

    @staticmethod
    def format_code_values(code_values, esri_type):
        if esri_type in ["esriFieldTypeString", "esriFieldTypeDate"]:
            return "'{0}'".format("','".join([str(c.get('code', -1)) for c in code_values]))
        else:
            return ",".join([str(c.get('code', -1)) for c in code_values])

    def _generate_check_domain_constraint_sql(self, domain):

        domain_type = domain['type']
        field_type = domain['fieldType']

        sql_template = self.db_client.sql_generator_templates.get(domain_type, "")
        p = {
            "field": self.db_client.sanitize_and_quote_name(domain['fieldName']),
            "values": ArcSet.format_code_values(domain.get('codedValues', []), field_type),
            "min_value": domain.get('minValue', 0),
            "max_value": domain.get('maxValue', 0)
        }
        sql = sql_template.format(**p)
        return sql

    def _generate_unique_constraint_sql(self, arc_index):
        """

        :param arc_index:
        :return:
        """
        if bool(arc_index.get('isUnique', False)):
            raise Exception("Index must be unique to be generated in this context!")

        if any([f['type'] == "esriFieldTypeGeometry" for f in self.fields if f['name'] == arc_index['fields']]):
            return ""

        p = {'idx_name': self.db_client.sanitize_name(arc_index['name']),
             'idx_fields': ",".join([self.db_client.sanitize_and_quote_name(f) for f in arc_index['fields'].split(",")]),
             'folder': self.db_client.sanitize_name(self.folder),
             'name': self.db_client.sanitize_name(self.name)}
        if any([f['type'] for f in self.fields
                if f['type'] == "esriFieldTypeOID" and arc_index['fields'] == f['name']]):
            return self.db_client.sql_generator_templates['unique_constraint'].format(**p)
        else:
            return self.db_client.sql_generator_templates['primary_constraint'].format(**p)

    def _generate_primary_key_constraint_sql(self, field):
        """

        :param field:
        :return:
        """
        if field['type'] != "esriFieldTypeOID":
            raise Exception("Field must be of type esriFieldTypeOID!")

        idx_name = self.db_client.sanitize_name(field['name'])
        p = {'idx_name': idx_name,
             'idx_fields':  ",".join([self.db_client.sanitize_and_quote_name(f) for f in idx_name.split(",")]),
             'folder': self.db_client.sanitize_name(self.folder),
             'name': self.db_client.sanitize_name(self.name)}
        return self.db_client.sql_generator_templates['primary_constraint'].format(**p)

    def _generate_index_sql(self, arc_index):
        """

        :param arc_index:
        :return:
        """
        if bool(arc_index.get('isUnique', False)):
            raise Exception("Unique constraints can not be generated in this context!")
        idx_name = self.db_client.sanitize_name(arc_index['name'])

        p = {'idx_name': idx_name,
             'idx_fields': ",".join([self.db_client.sanitize_and_quote_name(f) for f in arc_index['fields'].split(",")]),
             'folder': self.db_client.sanitize_name(self.folder),
             'name': self.db_client.sanitize_name(self.name)}

        if any([True for f in self.fields if f['name'] == arc_index['name'] and f['type'] == "esriFieldTypeGeometry"]
                + [False]):
            return ""
        else:
            return self.db_client.sql_generator_templates['create_index'].format(**p)

    def _index_fields_type_not_geometry(self, arc_index):
        fields = arc_index['fields'].split(",")
        result = [True for i, f in product(fields, self.fields)
                  if i == f['name'] and f['type'] == "esriFieldTypeGeometry"]
        return not any(result)

    def _generate_spatial_index_sql(self, field):
        """
        """
        if field['type'] != "esriFieldTypeGeometry":
            raise Exception("Spatial Index can not be generated for none geometry fields")

        p = {'idx_name': self.db_client.sanitize_name(self.name),
             'idx_fields': self.db_client.sanitize_and_quote_name(field['name']),
             'folder': self.db_client.sanitize_name(self.folder),
             'name': self.db_client.sanitize_name(self.name),
             'xmin': self.extent['xmin'],
             'ymin': self.extent['ymin'],
             'xmax': self.extent['xmax'],
             'ymax': self.extent['ymax']
             }

        return self.db_client.sql_generator_templates['create_spatial_index'].format(**p)

    def generate_sql(self):
        """

        :return: sql statement
        """

        try:
            sql_fields = ",\n".join(([self._generate_field_sql(f).strip() for f in self.fields]))
            sql_idx = ",\n".join(set([self._generate_unique_constraint_sql(f).strip() for f in self.fields
                                      if bool(f.get('isUnique', False))]))
            sql_checks = ",\n".join(set([self._generate_check_domain_constraint_sql(d) for d in self.domains]))
            pk_field = ([self._generate_primary_key_constraint_sql(f) for f in self.fields
                         if f['type'] == "esriFieldTypeOID"] + [None])[0]
            sql_constraints = ",\n".join([sql_idx] + [sql_checks])
            
            if pk_field is not None:
                sql_constraints += ",\n" + pk_field if sql_constraints.strip() != "," else pk_field
            else:
                raise Exception("Table {0}.{1} does not contains a primary key:  can not generate sql: {2}"
                                .format(self.folder, self.name, self.uri))

            p = {
                'table_name': self.sql_table_name, 
                'fields': sql_fields,
                'constraints': sql_constraints
            }
            sql = self.db_client.sql_generator_templates['drop_if_exists_create_table'].format(**p)

            idx = self.db_client.statement_terminator.join({self._generate_index_sql(i).strip() for i in self.indexes
                                                            if not bool(i.get('isUnique', False))
                                                            and self._index_fields_type_not_geometry(i)})
            sql += (self.db_client.statement_terminator if idx.strip() else "") + idx

            sp_idx = self.db_client.statement_terminator.join({self._generate_spatial_index_sql(i).strip()
                                                               for i in self.fields
                                                               if i.get('type', "") == "esriFieldTypeGeometry"})
            sql += (self.db_client.statement_terminator if sp_idx.strip() else "") + sp_idx.strip()

            return sql.strip()

        except Exception as e:
            self.add_error(e)
            return ""

    def generate_sql_extra(self):
        try:
            sql = self.db_client.statement_terminator.join([self._generate_code_table_relationships(d)
                                                            for d in self.domains
                                                            if bool(self._generate_code_table_relationships(d)
                                                                    .replace(self.db_client.statement_terminator, "")
                                                                    .strip())])
            if sql.replace(self.db_client.statement_terminator, '').strip() == "":
                return ""
            else:
                return sql.strip()
        except Exception as e:
            self.add_error(e)
            return ""

    def _generate_code_table_relationships(self, domain):
        p = {
            'schema': self.db_client.sanitize_and_quote_name(self.folder),
            'table_name': self.db_client.sanitize_and_quote_name(f"{self.name}"),
            'code_table_name': self.db_client.sanitize_and_quote_name(f"{self.name}_{domain['fieldName']}"),
            'column_name': self.db_client.sanitize_and_quote_name(f"{domain['fieldName']}"),
            'fk_name': self.db_client.sanitize_and_quote_name(f"FK_{self.folder}_{self.name}_{domain['fieldName']}")
        }
        sql_template = self.db_client.sql_generator_templates['code_table_foreign_key']
        sql = sql_template.format(**p)
        return sql

    def _generate_code_table(self, domain):
        max_length = max([len(c['name']) for c in domain.get('codedValues', [64])])

        code_field = f"{ self.db_client.sanitize_and_quote_name('Code')} " \
            f"{self.db_client.esri_types_to_sql[domain['fieldType']]} NOT NULL"
        if domain['fieldType'] == 'esriFieldTypeString':
            s = {
                'name': self.db_client.sanitize_and_quote_name('Code'),
                'type': self.db_client.esri_types_to_sql[domain['fieldType']],
                'length': max([len(c['code']) for c in domain.get('codedValues', [64])]),
                'null': 'NOT NULL'
            }
            code_field = self.db_client.sql_generator_templates[domain['fieldType']].format(**s)

        p = {
            'schema': self.db_client.sanitize_and_quote_name(self.folder),
            'table_name': self.db_client.sanitize_and_quote_name(f"{self.name}_{domain['fieldName']}"),
            'fields': self.db_client.sql_generator_templates['code_table_fields'].format(code_field=code_field,
                                                                                         max_length=max_length),
            'inserts': ",\n".join([self.db_client.sql_generator_templates['insert_code_table_row'].format(**code)
                                   for code in domain.get('codedValues', [])])
        }
        sql = self.db_client.sql_generator_templates['create_code_table_with_data'].format(**p)
        return sql

    def generate_sql_preamble(self):
        try:
            code_tables = self.db_client.statement_terminator.join([self._generate_code_table(d) for d in self.domains
                                                                    if bool(self._generate_code_table(d)
                                                                    .replace(self.db_client.statement_terminator, "")
                                                                            .strip())])
            if code_tables.replace(self.db_client.statement_terminator, "").strip() == "":
                return ""
            else:
                return code_tables.strip()

        except Exception as e:
            self.add_error(e)
            return ""

    def load_meta_data(self):
        try:
            self.load_json()
            self.loaded = True
        except Exception as e:
            self.add_error(e)
            self.loaded = False
        finally:
            return self.loaded
