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
                'header_sql': arc_layer.generate_sql_preamble(),
                'body_sql': arc_layer.generate_sql(),
                'footer_sql': arc_layer.generate_sql_extra(),
                'statement_terminator': arc_layer.db_client.statement_terminator
            }
            sql = "{header_sql}{statement_terminator}{body_sql}{statement_terminator}{footer_sql}".format(**p)

        # look from the layers and load their data
        loader = ArcSetDataLoader(arc_layer)
        loader.load_data()
        arc_layer.db_client.exec_non_query(sql)

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

    load_data_for_arc_layer(url, sql_server_conn, folder, create_db_objects=True)


if __name__ == "__main__":
    try:
        uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/PIPPIB_2020_Periode1/MapServer/0'  # url of arc service folder

        schema = "KLHK"  # schema name in database

        # database configuration for mssql
        # change server to match your server and database
        db_conn = {'server': '.\\npongo16',
                   'database': 'test_Indonesia_menlhk'}

        sql_server_conn = SqlServerClient(db_conn)  # create connection to ms sql server database
        # mysql_conn = MySQLClient(db_conn)  # create connection to ms sql server database
        # postgresql_conn = PostgreSQLClient(db_conn)  # create connection to ms sql server database

        load_data_for_arc_layer(uri, sql_server_conn, schema, create_db_objects=True)
    except Exception as e:
        exception_logging(e)
