from pickle import load
from urllib.parse import urlparse
from os import path
from json import dump
from _tests.secrets import db_conns
from db_clients.mysql_db_client import MySQLClient
from db_clients.postgresql_db_client import PostgreSQLClient
from db_clients.mssql_db_client import SqlServerClient


def get_db_conn(db_type):
    if db_type == "mssql":
        return SqlServerClient(db_conns[db_type])
    if db_type == 'mysql':
        return MySQLClient(db_conns[db_type])
    if db_type == "postgresql":
        return PostgreSQLClient(db_conns[db_type])
    return None


def mock_get_return(url):
    try:
        mock_json_dir = "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\responses"
        x = urlparse(url)
        file_name = f"{mock_json_dir}\\{x.netloc.replace('.','_')}_{'_'.join([s for s in x.path.replace('//','/').replace('/arcgis/rest','').replace('services','').split('/') if s != ''])}.json".replace("_.json", ".json").replace('_MapServer','')
        if not path.isfile(file_name):
            raise Exception(f"file not found {file_name}")
        resp = load(open(file_name, 'rb'))
        if url == "http://geoportal.menlhk.go.id/arcgis/rest":
            json = resp.json()
            json['folders'] = json['folder'][2:4]
            resp.text = dump(json)
        return resp
    except Exception as e:
        print(e)
        return None


def get_generated_sql_expected(file_name):
    sql_script_dir = "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output"
    path = f"{sql_script_dir}\\{file_name}"
    with open(path, 'r') as f:
        return f.read()


def save_test_to_file(file_name, content):
    sql_script_dir = "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output"
    path = f"{sql_script_dir}\\{file_name}"
    with open(path, 'w') as f:
        return f.write(content)