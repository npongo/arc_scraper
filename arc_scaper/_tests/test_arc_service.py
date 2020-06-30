from arc_service import ArcService
import requests
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, db_conn, get_generated_sql_expected, save_test_to_file
import pytest


@pytest.fixture(autouse=True)
def arc_service():
    uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV'
    folder = "SINAV"
    sql_conn = SqlServerClient(db_conn)
    return ArcService(uri, folder, "<dumpy arc rest model>", sql_conn)


def test_arc_service_init(monkeypatch, arc_service):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    arm = arc_service

    assert len(arm.errors) == 0
    assert len(arm.arc_map_servers) == 44


def test_arc_service_generate_sql(monkeypatch, arc_service):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_service
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


def test_arc_service_generate_sql_extra(monkeypatch, arc_service):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_service
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


def test_arc_service_generate_sql_preamble(monkeypatch, arc_service):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    service = arc_service
    sql = service.generate_sql_preamble()

    save_test_to_file("arc_service_generate_sql_preamble.txt", sql)
    sql_expected = get_generated_sql_expected("arc_service_generate_sql_preamble.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql_parse)
    except:
        assert False
