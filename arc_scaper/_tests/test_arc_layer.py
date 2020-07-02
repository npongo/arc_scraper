import requests
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_layer import ArcLayer
import pytest


@pytest.fixture(autouse=True)
def arc_layer(url, folder, db_type='mssql'):
    sql_client = get_db_conn(db_type)
    return ArcLayer(url, folder, sql_client)


def test_arc_layer_init(monkeypatch, arc_layer):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    assert len(layer.errors) == 0
    assert len(layer.fields) == 15
    assert layer.has_Z
    assert layer.has_M
    assert layer.geometry_field_name == "Shape"


@pytest.mark.parametrize("url, folder, expected", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV', '[SINAV].[dbklhk_pkps_pskl_usulan_iphps]'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN', '[KLHK_EN].[IUPHHK_RE]'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik', '[Publik].[Deforestasi_2017_2018]'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik', '[Publik].[IUPHHK_Hutan_Tanaman]')])
def test_arc_layer_sql_table_name(monkeypatch, arc_layer, expected):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql_name = arc_layer.sql_table_name
    assert sql_name == expected



@pytest.mark.parametrize("url, folder", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik')])
def test_arc_layer_generate_sql(monkeypatch, arc_layer):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql = layer.generate_sql()

    save_test_to_file("arc_set_generate_sql.txt", sql)
    sql_expected = get_generated_sql_expected("arc_set_generate_sql.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        arc_layer.db_client.exec_non_query(sql_parse)
    except:
        assert False


@pytest.mark.parametrize("url, folder", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik')])
def test_arc_layer_generate_sql_extra(monkeypatch, arc_layer):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql = layer.generate_sql_extra()

    save_test_to_file("arc_set_generate_sql_extra.txt", sql)
    sql_expected = get_generated_sql_expected("arc_set_generate_sql_extra.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        arc_layer.db_client.exec_non_query(sql_parse)
    except:
        assert False

@pytest.mark.parametrize("url, folder", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik')])
def test_arc_layer_generate_sql_preamble(monkeypatch, arc_layer):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql = layer.generate_sql_preamble()

    save_test_to_file("arc_set_generate_sql_preamble.txt", sql)
    sql_expected = get_generated_sql_expected("arc_set_generate_sql_preamble.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        arc_layer.db_client.exec_non_query(sql_parse)
    except:
        assert False
