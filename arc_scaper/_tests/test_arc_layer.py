import requests
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_layer import ArcLayer
import pytest


@pytest.fixture(autouse=True)
def arc_layer(url, folder, db_type):
    sql_client = get_db_conn(db_type)
    database = sql_client.db_conn['database']
    schema_quoted = sql_client.sanitize_and_quote_name(folder)
    sql_client.db_conn['database'] = sql_client.sql_generator_options['master_database']
    drop_database = sql_client.sql_generator_templates['drop_database'].format(database=folder)
    sql_client.exec_non_query(drop_database, autocommit=True)
    create_database = sql_client.sql_generator_templates['create_database'].format(database=folder)
    sql_client.exec_non_query(create_database, autocommit=True)
    sql_client.db_conn['database'] = database
    drop_schema = sql_client.sql_generator_templates['drop_schema'].format(schema=folder, schema_quoted=schema_quoted)
    sql_client.exec_non_query(drop_schema, autocommit=True)
    create_schema = sql_client.sql_generator_templates['create_schema'].format(schema=folder, schema_quoted=schema_quoted)
    sql_client.exec_non_query(create_schema, autocommit=True)
    return ArcLayer(url, folder, sql_client)


def test_arc_layer_init(monkeypatch, arc_layer):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    assert len(layer.errors) == 0
    assert len(layer.fields) == 15
    assert layer.has_Z
    assert layer.has_M
    assert layer.geometry_field_name == "Shape"



@pytest.mark.parametrize("url, folder, db_type, expected", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV', 'mssql', '[sinav].[usulan_iphps_dbklhk_pkps_pskl_usulan_iphps]'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN', 'mssql', '[KLHK_EN].[IUPHHK_RE_IUPHHK_RE]'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik', 'mssql', '[Publik].[def_2017_2018_publik_deforestasi_2017_2018]'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik', 'mssql', '[Publik].[iuphhk_ht_publik_iuphhk_hutan_tanaman]')])
def test_arc_layer_sql_table_name(monkeypatch, arc_layer, db_type, expected):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    sql_name = arc_layer.sql_full_table_name
    assert sql_name.lower() == expected.lower()



@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'postgresql')
                                                  ])
def test_arc_layer_generate_sql(monkeypatch, db_type, arc_layer):
    test_arc_layer_generate_sql_preamble(monkeypatch, db_type, arc_layer)
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql = layer.generate_sql()

    save_test_to_file(f"arc_set_generate_{db_type}.txt", sql)
    sql_expected = get_generated_sql_expected(f"arc_set_generate_{db_type}.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip()\
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        arc_layer.db_client.exec_non_query(sql, autocommit=True)
    except:
        assert False


@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'postgresql')
                                                  ])
def test_arc_layer_generate_sql_extra(monkeypatch,  db_type, arc_layer):
    test_arc_layer_generate_sql(monkeypatch, db_type, arc_layer)
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql = layer.generate_sql_extra()

    save_test_to_file("arc_set_generate_sql_extra.txt", sql)
    sql_expected = get_generated_sql_expected("arc_set_generate_sql_extra.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        arc_layer.db_client.exec_non_query(sql)
    except:
        assert False

@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'test', 'postgresql')
                                                  ])
def test_arc_layer_generate_sql_preamble(monkeypatch,  db_type, arc_layer):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    layer = arc_layer
    sql = layer.generate_sql_preamble()

    save_test_to_file("arc_set_generate_sql_preamble.txt", sql)
    sql_expected = get_generated_sql_expected("arc_set_generate_sql_preamble.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        arc_layer.db_client.exec_non_query(sql)
    except:
        assert False
