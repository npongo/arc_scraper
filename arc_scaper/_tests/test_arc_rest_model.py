from arc_rest_model import ArcRestModel
import requests
from os import path
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
import pytest


@pytest.fixture(autouse=True)
def arc_rest_model(db_type):
    uri = "http://geoportal.menlhk.go.id/arcgis/rest"
    database = 'test_Indonesia_menlhk'
    sql_client = get_db_conn(db_type)
    return ArcRestModel(uri, database, sql_client)


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_init(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_rest_model

    for e in arm.errors:
        print(e)
    assert len(arm.errors) == 2
    assert len(arm.arc_services) == 9

@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_generate_sql(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_rest_model
    sql = service.generate_sql()

    save_test_to_file(f"{arc_rest_model.db_client.name}_arc_service_generate_sql.sql", sql)
    sql_expected = get_generated_sql_expected(f"{arc_rest_model.db_client.name}_arc_service_generate_sql.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_generate_sql_extra(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_rest_model
    sql = service.generate_sql_extra()

    save_test_to_file(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_extra.sql", sql)
    sql_expected = get_generated_sql_expected(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_extra.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_generate_sql_preamble(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_rest_model
    sql = service.generate_sql_preamble()

    save_test_to_file(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_preamble.sql", sql)
    sql_expected = get_generated_sql_expected(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_preamble.sql")

    assert sql.strip() == sql_expected.strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False


@pytest.mark.parametrize("db_type, file", [('mssql', "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\MSSql_Script.sql"),
                                           ('mysql', "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\MySql_Script.sql"),
                                           ('postgresql', "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\PostgreSql_Script.sql")])
def test_save_sql_script(monkeypatch, arc_rest_model, file):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_rest_model
    arm.save_sql_script(file)

    assert path.isfile(file)


@pytest.mark.parametrize("db_type, db_master", [('mssql', 'master'),
                                                ('mysql', 'sys'),
                                                ('postgresql', 'postgres')])
def test_run_sql_script(monkeypatch, db_type, db_master, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_rest_model

    db = arc_rest_model.db_client.db_conn.get('database', 'Test_Indonesia_menlhk')
    sql = f'drop database {db}'
    if db_type == "mysql":
        sql = f"DROP DATABASE IF EXISTS {db}"
    if db_type == 'mssql':
        sql = f"IF DB_ID('{db}') IS NOT NULL DROP DATABASE {db}"
    arc_rest_model.db_client.db_conn['database'] = db_master
    arc_rest_model.db_client.exec_non_query(sql, autocommit=True)
    arc_rest_model.db_client.db_conn['database'] = db

    try:
        arm.run_sql(db_master=db_master)
    except:
        assert False

    sql = "select count(*) from sys.tables"
    result = arc_rest_model.db_client.exec_scalar_query(sql)
    assert result == 141