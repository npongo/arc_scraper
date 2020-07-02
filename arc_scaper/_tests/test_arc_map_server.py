import requests
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_map_server import ArcMapServer
import pytest


@pytest.fixture(autouse=True)
def arc_map_server(db_type='mssql'):
    uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer'
    folder = "SINAV"
    sql_client = get_db_conn(db_type)
    return ArcMapServer(uri, folder, "dumpy service",  sql_client)


def test_arc_map_server_init(monkeypatch, arc_map_server):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    map_server = arc_map_server

    assert len(map_server.errors) == 0
    assert len(map_server.layers) == 1


def test_arc_map_server_generate_sql(monkeypatch, arc_map_server):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    map_server = arc_map_server
    sql = map_server.generate_sql()

    save_test_to_file("arc_map_server_generate_sql.txt", sql)
    sql_expected = get_generated_sql_expected("arc_map_server_generate_sql.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        map_server.db_client.exec_non_query(sql_parse)
    except:
        assert False


def test_arc_map_server_generate_sql_extra(monkeypatch, arc_map_server):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    map_server = arc_map_server
    sql = map_server.generate_sql_extra()

    save_test_to_file("arc_map_server_generate_sql_extra.txt", sql)
    sql_expected = get_generated_sql_expected("arc_map_server_generate_sql_extra.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        map_server.db_client.exec_non_query(sql_parse)
    except:
        assert False


def test_arc_map_server_generate_sql_preamble(monkeypatch, arc_map_server):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    map_server = arc_map_server
    sql = map_server.generate_sql_preamble()

    save_test_to_file("arc_map_server_generate_sql_preamble.txt", sql)
    sql_expected = get_generated_sql_expected("arc_map_server_generate_sql_preamble.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        map_server.db_client.exec_non_query(sql_parse)
    except:
        assert False
