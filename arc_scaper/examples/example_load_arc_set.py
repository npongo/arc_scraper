from arc_layer import ArcLayer
from db_clients.mssql_db_client import SqlServerClient
from db_clients.mysql_db_client import MySQLClient
from db_clients.postgresql_db_client import PostgreSQLClient
from arc_set_data_loader import ArcSetDataLoader
from helpers import exception_logging


def load_data_for_arc_layer(uri, db_conn, schema, create_db_objects=False):
    try:
        arc_layer = ArcLayer(uri, schema, db_conn)  # create the arc service and load all the map servers and layers

        if create_db_objects:
            p = {
                'add_stats_table': '', # arc_layer.db_client.sql_generator_templates['create_stats_table'],  # comment out if stats table already exists in database
                'header_sql': arc_layer.generate_sql_preamble(),
                'body_sql': arc_layer.generate_sql(),
                'footer_sql': arc_layer.generate_sql_extra(),
                'statement_terminator': arc_layer.db_client.statement_terminator
            }
            sql = "{add_stats_table}{header_sql}{statement_terminator}{body_sql}{statement_terminator}{footer_sql}".format(**p)
            arc_layer.db_client.exec_non_query(sql)

        # look from the layers and load their data
        loader = ArcSetDataLoader(arc_layer)
        loader.load_data()

    except Exception as e:
        exception_logging(e)


def run_example():
    url = 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2020_Periode1/MapServer/0'  # url of arc service folder

    folder = "KLHK"  # schema name in database

    # database configuration for mssql
    # change server to match your server and database
    sql_conn = {'server': '.\\npongo16',
               'database': 'test_Indonesia_menlhk'}

    sql_server_conn = SqlServerClient(sql_conn)  # create connection to ms sql server database
    # mysql_conn = MySQLClient(db_conn)  # create connection to ms sql server database
    # postgresql_conn = PostgreSQLClient(db_conn)  # create connection to ms sql server database

    # create table and load records into table
    # load_data_for_arc_layer(uri, sql_server_conn, schema, create_db_objects=True)

    # only load records into table
    load_data_for_arc_layer(uri, sql_server_conn, schema, create_db_objects=False)


if __name__ == "__main__":
    try:

        uris = ['http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2014/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2015/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2016/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2017/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2018/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2019/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Pelepasan_Kawasan_Hutan/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Pelepasan_Kawasan_Hutan_untuk_Transmigrasi/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2019/MapServer/0'
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Pinjam_Pakai_Kawasan_Hutan/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIAPS_V/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/RekalkulasiBatasKawasan/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIAPS_Rev4/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/RHL_2014/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/RHL_2015/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/RHL_2016/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/WilayahPengukuranKinerja_REDD/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/KPH/MapServer/1',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2020_Periode1/MapServer/0',  # url of arc service folder
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Ekoregion_Darat_Laut/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/KHG/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Kawasan_Hutan/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/HOTSPOT_2014/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/HOTSPOT_2015/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/HOTSPOT_2016/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/HOTSPOT_2017/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/HOTSPOT_2018/MapServer/0',
                'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/HOTSPOT_2019/MapServer/0']

        # uris = ['http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Lahan_Kritis_2018/MapServer/0']

        schema = "KLHK"  # schema name in database

        # database configuration for mssql
        # change server to match your server and database
        db_conn = {'server': '.\\npongo16',
                   'database': 'test_Indonesia_menlhk'}

        sql_server_conn = SqlServerClient(db_conn)  # create connection to ms sql server database
        # mysql_conn = MySQLClient(db_conn)  # create connection to ms sql server database
        # postgresql_conn = PostgreSQLClient(db_conn)  # create connection to ms sql server database

        # create table and load records into table
        #load_data_for_arc_layer(uri, sql_server_conn, schema, create_db_objects=True)

        # only load records into table
        for uri in uris:
            load_data_for_arc_layer(uri, sql_server_conn, schema, create_db_objects=False)
    except Exception as e:
        exception_logging(e)
