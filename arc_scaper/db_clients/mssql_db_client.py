import pymssql
from helpers import sanitize_and_quote_name, exception_logging


class SqlServerClient:

    def __init__(self, db_conn, sql_generator_options={}, sql_generator_templates={}):
        self.__db_conn = db_conn
        self.__sql_generator_templates = {
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
            "insert_stats": "INSERT INTO TableStats(TableName, MinOID, MaxOID, RecordCount, LoadedRecordCount) VALUES('{table_name}',{min_OID},{max_OID},{record_count},{loaded_record_count}}",
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
            "insert_stats": "INSERT INTO ArcSetStats(TableName,LoadDate,MinOID,MaxOID,RecordCount,LoadedRecordCount,JsonDef,errors)VALUES('{table_name}', '{timestamp}', {min_OID}, {max_OID}, {record_count}, {loaded_record_count}, '{json}', '{errors}')",
            "create_stats_table": "CREATE TABLE ArcSetStats(\nTableName varchar(128)\n,LoadDate datetime NOT NULL\n,MinOID int NULL\n,MaxOID int NULL\n,RecordCount int NULL\n,LoadedRecordCount int NULL\n,JsonDef varchar(max) NULL\n,errors varchar(512) NULL\n,CONSTRAINT PK_ArcSetStats PRIMARY KEY(TableName, LoadDate)\n) "
        }

        for k, v in sql_generator_templates:
            self.__sql_generator_templates[k] = v

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

        self.__sql_generator_options = {
            'enforce_relationships': False,
            'enforce_domains': True,
            "statement_terminator": "\nGO\n\n",
            "quote_characters": '[]',
            "max_identifier_length": 128
        }

        for k, v in sql_generator_options:
            self.__sql_generator_options[k] = v

    @property
    def name(self):
        return "mssql_db_client"

    @property
    def sql_generator_templates(self):
        return self.__sql_generator_templates

    @sql_generator_templates.setter
    def sql_generator_templates(self, value):
        for k, v in value:
            self.__sql_generator_templates[k] = v

    @property
    def sql_generator_options(self):
        return self.__sql_generator_options

    @sql_generator_options.setter
    def sql_generator_options(self, value):
        for k, v in value:
            self.__sql_generator_options[k] = v

    @property
    def db_conn(self):
        return self.__db_conn

    @db_conn.setter
    def db_conn(self, value):
        self.__db_conn = value

    def quote_name(self, name):
        quote_start = self.quote_characters[0]
        quote_end = (self.quote_characters + self.quote_characters)[1]
        if not name.startswith(quote_start):
            name = quote_start + name
        if not name.endswith(quote_end):
            name += quote_end
        return name

    def sanitize_and_quote_name(self, name):
        return sanitize_and_quote_name(name, self.quote_characters)

    @property
    def statement_terminator(self):
        return self.__sql_generator_options.get('statement_terminator','\nGO\n\n')

    @property
    def quote_characters(self):
        return self.__sql_generator_options.get("quote_characters", "[]")

    def exec_non_query(self, sql_statements, autocommit=False):
        """

        :param sql_statements: a list of sql statements to execute that doe not return a result, primaryily meant for DDL slq
        :param autocommit: control the autocommit feature of the connection.
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
                cursor.execute(stm.strip())

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

    @staticmethod
    def chunker(seq, size):
        """
        groups a list into a list of chunks
        :param seq: input sequence or list
        :param size: sizs of the chunk to group the seq into
        :return: a list of lists, the inner list has the length of size
        """
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

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


