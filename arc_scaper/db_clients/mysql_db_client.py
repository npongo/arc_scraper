from mysql.connector import connect, Error
from helpers import sanitize_and_quote_name, exception_logging, sanitize_name
from datetime import datetime
from db_clients.db_client_base import DBClient


class MySQLClient(DBClient):

    def __init__(self, db_conn, sql_generator_options={}, sql_generator_templates={}):

        super().__init__(db_conn)

        self._sql_generator_templates = {
            "table_name": "{schema}.{table_name}",
            "null_string": "NULL",
            "esriFieldTypeOID": "{name} {type} NOT NULL",
            "esriFieldTypeString": "{name} {type}({length}) {null}",
            "esriFieldTypeDate": "`{name}` {type} {null}, \n `{name}_date` datetime AS (FROM_UNIXTIME({name}/1000)) NULL",
            "unique_field": "NOT NULL UNIQUE",
            "unique_constraint": "CONSTRAINT `{schema}_{name}_{idx_name}` UNIQUE({idx_fields})",
            "primary_constraint": "CONSTRAINT `pk_{schema}_{name}_{idx_name}` PRIMARY KEY({idx_fields})",
            "create_spatial_index": "ALTER TABLE  `{schema}`.`{table_name}` ADD SPATIAL INDEX({idx_fields})",
            "create_index": "CREATE INDEX `{schema}_{name}_{idx_name}` ON `{schema}`.`{table_name}`({idx_fields})",
            "foreign_key_constraint": "ALTER TABLE {schema}.{table_name}\nADD CONSTRAINT `fk_{name}` FOREIGN KEY({column}) REFERENCES {ref_schema}.{ref_table_name} ({ref_column})",
            "create_schema": "CREATE SCHEMA IF NOT EXISTS {schema_quoted}",
            "drop_schema": "",  # "DROP SCHEMA IF EXISTS {schema_quoted}",
            "rangeValue": "CONSTRAINT `ck_{table_name}_{field}_range_domain` CHECK({field_quoted} BETWEEN {min_value} AND {max_value})",
            "codedValue": "CONSTRAINT `ck_{table_name}_{field}_code_domain` CHECK({field_quoted} IN({values}))",
            "select_object_ids": "SELECT {object_id_field_name} FROM {table_name}",
            "data_insert": "INSERT INTO {table_name}({columns}) VALUES {values}",
            "data_row_insert": "({values})",
            "spatial_data_insert": "(ST_GeomFromText('{wkt}',4326, 'axis-order=long-lat'), {values})",
            "null_spatial_data_insert": "({values},NULL)",
            "create_database": "CREATE DATABASE IF NOT EXISTS {database};\n\nUSE {database}",
            "drop_database": "DROP DATABASE IF EXISTS {database}",
            "drop_if_exists_create_table": "DROP TABLE IF EXISTS {table_name};\n\nCREATE TABLE {table_name} (\n{fields}{constraints}\n)",
            "create_code_table_with_data": "DROP TABLE IF EXISTS {schema}.{table_name};\n\nCREATE TABLE {schema}.{table_name} (\n{fields}\n);\n\nINSERT INTO{schema}.{table_name}(`code`, `name`)VALUES\n{inserts}",
            "code_table_fields": "{code_field} PRIMARY KEY,\n`name` nvarchar({max_length}) NOT NULL",
            "insert_code_table_row": "('{code}', '{name}')",
            "code_table_foreign_key": "ALTER TABLE {schema}.{table_name}\nADD CONSTRAINT {fk_name} FOREIGN KEY({column_name}) REFERENCES {schema}.{code_table_name}(`code`)",
            "truncate_table": "TRUNCATE TABLE {table_name}",
            "insert_stats": "INSERT INTO arc.arc_set_stats(table_name,load_date,min_oid,max_oid,record_count,loaded_record_count,arc_set_url,json_def,errors)VALUES('{table_name}', '{timestamp}', {min_OID}, {max_OID}, {record_count}, {loaded_record_count}, '{url}', '{json}', {errors})",
            "create_stats_table": "CREATE SCHEMA IF NOT EXISTS `arc`;\n\nDROP TABLE IF EXISTS `arc`.`arc_set_stats`;\n\nCREATE TABLE `arc`.`arc_set_stats`(\n`table_name` varchar(128)\n,`load_date` datetime NOT NULL\n,`min_oid` int NULL\n,`max_oid` int NULL\n,`record_count` int NULL\n,`loaded_record_count` int NULL\n,`arc_set_url` varchar(512) NULL\n,`json_def` MEDIUMTEXT NULL\n,`errors` varchar(512) NULL\n,CONSTRAINT `pk_arc_set_stats` PRIMARY KEY(`table_name`, `load_date`)\n)",
            "create_error_table": 'CREATE SCHEMA IF NOT EXISTS `arc`;\n\nDROP TABLE IF EXISTS `arc`.`errors`;\n\nCREATE TABLE IF NOT EXISTS `arc`.`errors`(`id` MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, `error_message` text NULL, `error_type` varchar(128) NULL, `line_no` int NULL, `file_name` text NULL)',
            "insert_error": "INSERT INTO arc.errors('error_message', 'error_type', 'line_no', 'file_name') VALUES({error_message}, {error_type}, {line_no}, {file_name})"

        }

        for k, v in sql_generator_templates:
            self.sql_generator_templates[k] = v

        self.esri_types_to_sql = {"esriFieldTypeSmallInteger": "smallint",
                     "esriFieldTypeSingle": "float",
                     "esriFieldTypeString": "varchar",
                     "esriFieldTypeDate": "bigint",
                     "esriFieldTypeGeometry": "geometry",
                     "esriFieldTypeOID": "int",
                     "esriFieldTypeBlob": "blob",
                     "esriFieldTypeGlobalID": "char(36)",
                     "esriFieldTypeRaster": "varbinary",
                     "esriFieldTypeGUID": "char(36)",
                     "esriFieldTypeXML": "longtext",
                     "esriFieldTypeDouble": "double",
                     "esriFieldTypeInteger": "int"}

        self._sql_generator_options = {
            'enforce_relationships': False,
            'enforce_domains': True,
            "statement_terminator": ";\n\n",
            "quote_characters": "`",
            "max_identifier_length": -63,
            "use_lower_case_identifier": True,
            "allow_double_symbols": True,
            'insert_safe_characters': {"'": "''"},
            'sanitize_replacements': {'': u"`~!@#$%^*()+=][{}\\|?><,/;:'\"",
                                      "_": u".-& "},
            'name': "mysql_db_client",
            'master_database': 'sys',
            'date_string_format': "%Y-%m-%dT%H:%M:%S",
            'text_qoute': "'",
            'escape_characters': {"'": "''"}
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
        conn = connect(**self.db_conn)
        conn.autocommit = autocommit
        cursor = conn.cursor()
        try:
            if not isinstance(sql_statements, list):
                sql_statements = [s for s in sql_statements.split(self.statement_terminator) if s.strip()]

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
        conn = connect(**self.db_conn)
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
        conn = connect(**self.db_conn)
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
        conn = connect(**self.db_conn)
        cursor = conn.cursor()
        i = 0
        try:
            formatted = [formatter(row) for row in data]
            for inserts in MySQLClient.chunker(formatted, batch):
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
