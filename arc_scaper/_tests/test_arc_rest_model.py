from arc_rest_model import ArcRestModel
import requests
from db_clients.mssql_db_client import SqlServerClient
from os import path
from _tests.mock_helper import mock_get_return, db_conn, get_generated_sql_expected, save_test_to_file
import pytest


@pytest.fixture(autouse=True)
def arc_rest_model():
    uri = "http://geoportal.menlhk.go.id/arcgis/rest"
    database = 'test_Indonesia_menlhk'
    sql_conn = SqlServerClient(db_conn)
    return ArcRestModel(uri, database, sql_conn)


def test_arc_rest_model_init(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_rest_model

    for e in arm.errors:
        print(e)
    assert len(arm.errors) == 2
    assert len(arm.arc_services) == 9


def test_arc_rest_model_generate_sql(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_rest_model
    sql = service.generate_sql()

    save_test_to_file("arc_service_generate_sql.txt", sql)
    sql_expected = get_generated_sql_expected("arc_service_generate_sql.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False


def test_arc_rest_model_generate_sql_extra(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_rest_model
    sql = service.generate_sql_extra()

    save_test_to_file("arc_service_generate_sql_extra.txt", sql)
    sql_expected = get_generated_sql_expected("arc_service_generate_sql_extra.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False


def test_arc_rest_model_generate_sql_preamble(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_rest_model
    sql = service.generate_sql_preamble()

    save_test_to_file("arc_service_generate_sql_preamble.txt", sql)
    sql_expected = get_generated_sql_expected("arc_service_generate_sql_preamble.txt")

    assert sql.strip() == sql_expected.strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False


def test_save_sql_script(monkeypatch, arc_rest_model):
    file = "C:\\Users\\npongo\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\Script.sql"
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_rest_model

    arm.save_sql_script(file)

    assert path.isfile(file)


def test_run_sql_script(monkeypatch, arc_rest_model):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_rest_model

    db = arc_rest_model.db_client.db_conn.get('database', 'Test_Indonesia_menlhk')
    sql = f"IF DB_ID('{db}') IS NOT NULL DROP DATABASE {db}"
    arc_rest_model.db_client.db_conn['database'] = 'master'
    arc_rest_model.db_client.exec_non_query(sql, autocommit=True)
    arc_rest_model.db_client.db_conn['database'] = db

    try:
        arm.run_sql()
    except:
        assert False

    sql = "select count(*) from sys.tables"
    result = arc_rest_model.db_client.exec_scalar_query(sql)
    assert result == 141
