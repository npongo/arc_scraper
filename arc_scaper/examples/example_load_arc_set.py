from arc_layer import ArcLayer
from db_clients.mssql_db_client import SqlServerClient
from db_clients.mysql_db_client import MySQLClient
from db_clients.postgresql_db_client import PostgreSQLClient
from arc_set_data_loader import ArcSetDataLoader
from helpers import exception_logging


def create_db_objects(schema, db_client):

    add_arc_schema = db_client.sql_generator_templates['create_schema'].format(schema='Arc', schema_quoted='[Arc]')
    add_stats_table = db_client.sql_generator_templates['create_stats_table']  # comment out if stats table already exists in database
    add_erorr_table = db_client.sql_generator_templates['create_error_table']
    add_folder_schema = db_client.sql_generator_templates['create_schema'].format(schema=schema, schema_quoted=schema)
    statement_terminator = db_client.statement_terminator

    sql = f"{add_arc_schema}{statement_terminator}{add_stats_table}{statement_terminator}{add_erorr_table}{statement_terminator}{add_folder_schema}"
    db_client.exec_non_query(sql, autocommit=True)  # set autocommit to True to run DDL


def load_data_for_arc_layer(params, db_client, schema, create_db_objects=False, load_data=True):
    try:
        uri = params['uri']
        arc_layer = ArcLayer(uri, schema, db_client)  # create the arc service and load all the map servers and layers
        del params['uri']

        if create_db_objects:
            header_sql = arc_layer.generate_sql_preamble()
            body_sql = arc_layer.generate_sql()
            footer_sql = arc_layer.generate_sql_extra()
            statement_terminator = arc_layer.db_client.statement_terminator

            sql = f"{header_sql}{statement_terminator}{body_sql}{statement_terminator}{footer_sql}"
            arc_layer.db_client.exec_non_query(sql, autocommit=True)  # set autocommit to True to run DDL

        # look from the layers and load their data
        if load_data:
            loader = ArcSetDataLoader(arc_layer, **params)
            loader.load_data()

    except Exception as e:
        exception_logging(e)


def run_example():
    url = 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2020_Periode1/MapServer/0'  # url of arc service folder

    schema = "KLHK"  # schema name in database

    # database configuration for mssql
    # change server to match your server and database
    sql_conn = {'server': '.\\npongo16',
               'database': 'Indonesia_menlhk'}

    db_client = SqlServerClient(sql_conn)  # create connection to ms sql server database
    # db_client = MySQLClient(db_conn)  # create connection to ms sql server database
    # db_client = PostgreSQLClient(db_conn)  # create connection to ms sql server database

    # create table and load records into table
    # load_data_for_arc_layer(uri, db_client, schema, create_db_objects=True)

    # only load records into table
    load_data_for_arc_layer(uri, db_client, schema, create_db_objects=False)


if __name__ == "__main__":
    try:

        uris = [
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2015/MapServer/0',
                 'result_record_count': 2,
                 'max_result_record_count': 10,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 30
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2018_/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 30
                 },
                {'uri':  'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2019/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2014/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },

                 {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Pelepasan_Kawasan_Hutan/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Pelepasan_Kawasan_Hutan_untuk_Transmigrasi/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },

                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2019/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2020_Periode1/MapServer/0',  # url of arc service folder
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Pinjam_Pakai_Kawasan_Hutan/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIAPS_V/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/RekalkulasiBatasKawasan/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIAPS_Rev4/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/WilayahPengukuranKinerja_REDD/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },

                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Ekoregion_Darat_Laut/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Ekoregion_Darat/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Fungsi_Ekologi_Gambut/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/IUPHHK_HTI/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri':  'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/IUPHHK_RE/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri':  'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/IUPHHK_HA/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },

                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/KHG/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/KPH/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/KPH/MapServer/1',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },

                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Kawasan_Hutan/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Hutan_Adat/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Hutan_Desa/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Hutan_Kemasyarakatan/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Hutan_Mangrove/MapServer/1',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                {'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Hutan_Tanaman_Rakyat/MapServer/0',
                 'result_record_count': 10,
                 'max_result_record_count': 100,
                 'max_tries': 1,
                 'target_time': 50000,
                 'timeout': 10
                 },
                ]

        # uris = ['http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Lahan_Kritis_2018/MapServer/0']

        schema = "KLHK"  # schema name in database

        # database configuration for mssql
        # change server to match your server and database
        # database needs to exist
        db_conn = {'server': '.\\npongo16',
                   'database': 'Indonesia_menlhk'}

        db_client = SqlServerClient(db_conn)  # create connection to ms sql server database
        # db_client = MySQLClient(db_conn)  # create connection to ms sql server database
        # db_client = PostgreSQLClient(db_conn)  # create connection to ms sql server database

        # create table and load records into table
        # create_db_objects(schema, db_client) #  use this method to create stats and error logging tables.
        # for uri in uris:
        #    load_data_for_arc_layer(uri, db_client, schema, create_db_objects=True,  load_data=False)

        # only load records into table
        for uri in uris:
            load_data_for_arc_layer(uri, db_client, schema, create_db_objects=False,  load_data=True)
    except Exception as e:
        exception_logging(e)
