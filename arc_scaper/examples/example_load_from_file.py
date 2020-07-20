
from arc_layer import ArcLayer
from db_clients.mssql_db_client import SqlServerClient
from db_clients.mysql_db_client import MySQLClient
from db_clients.postgresql_db_client import PostgreSQLClient
from arc_set_data_loader import ArcSetDataLoader
from helpers import exception_logging
from json import dumps, load

def load_data_for_arc_layer(params, db_client, schema, file_path):
    try:
        p = params.copy()
        uri = p['uri']
        arc_layer = ArcLayer(uri, schema, db_client)  # create the arc service and load all the map servers and layers
        del p['uri']


        # look from the layers and load their data

        loader = ArcSetDataLoader(arc_layer, **p)

        with open(file_path, 'r') as f:
            # content = f.read()
            json = load(f)
        loader.parse_and_save_json_data(json)
    except Exception as e:
        exception_logging(e)


def run_example():
    try:

        arc_set = {
            'uri': 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK/Penutupan_Lahan_Tahun_2017_/MapServer/0',
            'result_record_count': 1,
            'max_result_record_count': 100,
            'max_tries': 2,
            'target_time': 1500000,
            'timeout': 1500,
            'max_allowable_offset': 1025,
            'geometry_precision': 7
            }

        # path to a json file that is the output of an arc map service query
        file_path = ".\\Penutupan_Lahan_Tahun_2017_337.json"
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
        load_data_for_arc_layer(arc_set, db_client, schema, file_path)
    except Exception as e:
        exception_logging(e)


if __name__ == "__main__":
    try:
        run_example()
    except Exception as e:
        exception_logging(e)
