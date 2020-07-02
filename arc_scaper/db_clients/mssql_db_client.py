import pymssql
from helpers import sanitize_and_quote_name, exception_logging, sanitize_name
from datetime import datetime
from db_clients.db_client_base import DBClient


class SqlServerClient(DBClient):

    def __init__(self, db_conn, sql_generator_options={}, sql_generator_templates={}):

        super().__init__(db_conn)

        self._sql_generator_templates = {
            "table_name": "{schema}.{table_name}",
            "null_string": "NULL",
            "esriFieldTypeOID": "{name} {type} NOT NULL",
            "esriFieldTypeString": "{name} {type}({length}) {null}",
            "esriFieldTypeDate": "[{name}] {type} {null}, \n[{name}_Date] AS (dateadd(millisecond, {name}%(60000), dateadd(minute, {name}/(60000), '1970-01-01 00:00:00.000')))",
            "unique_field": "NOT NULL UNIQUE",
            "unique_constraint": "CONSTRAINT [{folder}_{name}_{idx_name}] UNIQUE([{idx_fields}])",
            "primary_constraint": "CONSTRAINT [pk_{folder}_{name}_{idx_name}] PRIMARY KEY([{idx_fields}])",
            "create_spatial_index": "CREATE SPATIAL INDEX [spidx_{folder}_{idx_name}_{idx_fields}] ON [{folder}].[{idx_name}]({idx_fields}) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = {xmin},  ymin = {ymin},  xmax = {xmax},  ymax = {ymax})); ",
            "create_index": "CREATE INDEX [{folder}_{name}_{idx_name}] ON [{folder}].[{name}]({idx_fields})",
            "foreign_key_constraint": "ALTER TABLE {schema}.{table_name}\nADD CONSTRAINT [fk_{name}] FOREIGN KEY({column}) REFERENCES {ref_schema}.{ref_table_name} ({ref_column})",
            "create_schema": "IF SCHEMA_ID('{schema}') IS NULL EXEC('CREATE SCHEMA [{schema}]')",
            "rangeValue": "CONSTRAINT [CK_{field}_range_domain] CHECK([{field}] BETWEEN {min_value} AND {max_value})",
            "codedValue": "CONSTRAINT [CK_{field}_code_domain] CHECK([{field}] IN({values}))",
            "select_object_ids": "SELECT {object_id_field_name} FROM {table_name}",
            "data_insert": "INSERT INTO {table_name}({columns}) VALUES {values}",
            "data_row_insert": "({values})",
            "spatial_data_insert": "({values}, GEOMETRY::STGeomFromText('{wkt}',4326))",
            "null_spatial_data_insert": "({values},NULL)",
            "create_database": "USE master\nGO\n\nIF DB_ID('{database}') IS NULL CREATE DATABASE {database}\nGO\n\nUSE [{database}]",
            "drop_if_exists_create_table": "IF OBJECT_ID('{table_name}') IS NOT NULL\n\tDROP TABLE {table_name}\nGO\n\nCREATE TABLE {table_name} (\n{fields}{constraints}\n)",
            "create_code_table_with_data": "IF OBJECT_ID('{schema}.{table_name}') IS NOT NULL\n\tDROP TABLE {schema}.{table_name}\nGO\n\nCREATE TABLE {schema}.{table_name} (\n{fields}\n)\nGO\n\nINSERT INTO{schema}.{table_name}([Code], [Name])VALUES\n{inserts}",
            "code_table_fields": "{code_field} PRIMARY KEY,\n[Name] nvarchar({max_length}) NOT NULL",
            "insert_code_table_row": "('{code}', '{name}')",
            "code_table_foreign_key": "ALTER TABLE {schema}.{table_name}\nADD CONSTRAINT {fk_name} FOREIGN KEY({column_name}) REFERENCES {schema}.{code_table_name}(Code)",
            "truncate_table": "TRUNCATE TABLE {table_name}",
            "insert_stats": "INSERT INTO Arc.ArcSetStats(TableName,LoadDate,MinOID,MaxOID,RecordCount,LoadedRecordCount,ArcSetUrl,JsonDef,errors)VALUES('{table_name}', '{timestamp}', {min_OID}, {max_OID}, {record_count}, {loaded_record_count}, '{url}', '{json}', {errors})",
            "create_stats_table": "IF SCHEMA_ID('{schema}') IS NULL EXEC('CREATE SCHEMA [Arc]')\nGO\n\nCREATE TABLE Arc.ArcSetStats(\nTableName varchar(128)\n,LoadDate datetime NOT NULL\n,MinOID int NULL\n,MaxOID int NULL\n,RecordCount int NULL\n,LoadedRecordCount int NULL\n,ArcSetUrl varchar(512) NULL\n,JsonDef varchar(max) NULL\n,errors varchar(512) NULL\n,CONSTRAINT PK_ArcSetStats PRIMARY KEY(TableName, LoadDate)\n) "
        }

        for k, v in sql_generator_templates:
            self._sql_generator_templates[k] = v

        self.esri_types_to_sql = {"esriFieldTypeSmallInteger": "smallint",
                     "esriFieldTypeSingle": "real",
                     "esriFieldTypeString": "varchar",
                     "esriFieldTypeDate": "bigint",
                     "esriFieldTypeGeometry": "geometry",
                     "esriFieldTypeOID": "int",
                     "esriFieldTypeBlob": "varbinary",
                     "esriFieldTypeGlobalID": "uniqueidentifier",
                     "esriFieldTypeRaster": "varbinary",
                     "esriFieldTypeGUID": "uniqueidentifier",
                     "esriFieldTypeXML": "XML",
                     "esriFieldTypeDouble": "float",
                     "esriFieldTypeInteger": "int"}

        self._sql_generator_options = {
            'enforce_relationships': False,
            'enforce_domains': True,
            "statement_terminator": "\nGO\n\n",
            "quote_characters": '[]',
            "max_identifier_length": -128,
            "use_lower_case_identifier": False,
            'date_string_format': "%Y-%m-%dT%H:%M:%S",
            'insert_safe_characters': {"'": "''"},
            'sanitize_replacements': {'': u"`~!@#$%^*()+=][{}\\|?><,/;:'\"",
                                      "_": u".-& "},
            'name': 'mssql_db_client'
        }

        for k, v in sql_generator_options:
            self._sql_generator_options[k] = v
    
    def exec_non_query(self, sql_statements, autocommit=False, raise_on_fail=False):
        """

        :param sql_statements: a list of sql statements to execute that doe not return a result, primaryily meant for DDL slq
        :param autocommit: control the autocommit feature of the connection.
        :param raise_on_fail: stops execture of additional sql statements if true and raise the exception, otherwise
        exceptions are logged
        :return: None
        """
        conn = pymssql.connect(**self.db_conn)
        if autocommit:
            conn.autocommit(True)
        cursor = conn.cursor()
        try:
            if not isinstance(sql_statements, list):
                sql_statements = sql_statements.split(self.statement_terminator)

            for stm in sql_statements:
                try:
                    cursor.execute(stm.strip())
                except Exception as e:
                    exception_logging(e)
                    if raise_on_fail:
                        raise e

            if not autocommit:
                conn.commit()

        except Exception as e:
            conn.rollback()
            exception_logging(e)
            raise e
        finally:
            cursor.close()
            conn.close()

    def exec_scalar_query(self, sql_statement):
        """
        execute an sql query against the sql server database that returns a scalar value
        :param sql_statement: an sql statement that returns a scalar value
        :return: scaler
        """
        conn = pymssql.connect(**self.db_conn)
        cursor = conn.cursor()
        try:
            cursor.execute(sql_statement)
            result = cursor.fetchone()[0]
            conn.commit
            return result
        except Exception as e:
            conn.rollback()
            exception_logging(e)
            raise e
        finally:
            cursor.close()
            conn.close()

    def exec_result_set_query(self, sql_statement):
        """
        execute an sql query against the sql server database that returns a scalar value
        :param sql_statement: an sql statement that returns a scalar value
        :return: scaler
        """
        conn = pymssql.connect(**self.db_conn)
        cursor = conn.cursor()
        try:
            cursor.execute(sql_statement)
            result = [r for r in cursor]
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            exception_logging(e)
            raise e
        finally:
            cursor.close()
            conn.close()

    def run_bulk_insert(self, insert_template, data, formatter, batch=1000):
        """

        :param insert_template: template used to insert data
        :param data: iterable of rows of data
        :param formatter: function used to format row of data
        :param batch:
        :return:
        """
        conn = pymssql.connect(**self.db_conn)
        cursor = conn.cursor()
        i = 0
        try:
            formatted = [formatter(row) for row in data]
            for inserts in SqlServerClient.chunker(formatted, batch):
                sql_stm = insert_template.format(",".join(inserts))
                try:
                    cursor.execute(sql_stm)
                    i += len(inserts)
                    conn.commit()
                except Exception as e:
                    if batch == 1:
                        raise Exception(f"Error inserting {sql_stm} with exception {e}")
                    else:  # run individual
                        self.run_bulk_insert(insert_template, inserts, formatter, batch=1)

        except Exception as e:
            conn.rollback()
            exception_logging(e)
            raise(e)

        finally:
            cursor.close()
            conn.close()
            return i


