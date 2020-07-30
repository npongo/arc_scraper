import requests
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_map_server import ArcMapServer
import pytest


@pytest.fixture(autouse=True)
def arc_map_server(monkeypatch, url, folder, db_type):
    monkeypatch.setattr(requests, 'get', mock_get_return)

    sql_client = get_db_conn(db_type)
    database = sql_client.db_conn['database']
    schema_quoted = sql_client.sanitize_and_quote_name(folder)
    sql_client.db_conn['database'] = sql_client.sql_generator_options['master_database']
    drop_database = sql_client.sql_generator_templates['drop_database'].format(database=database)
    sql_client.exec_non_query(drop_database, autocommit=True)
    create_database = sql_client.sql_generator_templates['create_database'].format(database=database)
    sql_client.exec_non_query(create_database, autocommit=True)
    sql_client.db_conn['database'] = database
    drop_schema = sql_client.sql_generator_templates['drop_schema'].format(schema=folder, schema_quoted=schema_quoted)
    sql_client.exec_non_query(drop_schema, autocommit=True)
    create_schema = sql_client.sql_generator_templates['create_schema'].format(schema=folder, schema_quoted=schema_quoted)
    sql_client.exec_non_query(create_schema, autocommit=True)

    return ArcMapServer(url, folder, "dumpy service",  sql_client)


@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'postgresql')
                                                  ])
def test_arc_map_server_init(arc_map_server):
    map_server = arc_map_server

    assert len(map_server.errors) == 0
    assert len(map_server.layers) == 1


@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'postgresql')
                                                  ])
def test_arc_map_server_generate_sql(arc_map_server):
    map_server = arc_map_server
    sql = map_server.generate_sql()

    save_test_to_file("arc_map_server_generate_sql.txt", sql)
    sql_expected = get_generated_sql_expected("arc_map_server_generate_sql.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    #sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        map_server.db_client.exec_non_query(sql)
    except:
        assert False

@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'postgresql')
                                                  ])
def test_arc_map_server_generate_sql_extra(arc_map_server):
    map_server = arc_map_server
    sql = map_server.generate_sql_extra()

    save_test_to_file("arc_map_server_generate_sql_extra.txt", sql)
    sql_expected = get_generated_sql_expected("arc_map_server_generate_sql_extra.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        map_server.db_client.exec_non_query(sql)
    except:
        assert False

@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer', 'test', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer', 'test', 'postgresql')
                                                  ])
def test_arc_map_server_generate_sql_preamble(arc_map_server):
    map_server = arc_map_server
    sql = map_server.generate_sql_preamble()

    save_test_to_file("arc_map_server_generate_sql_preamble.txt", sql)
    sql_expected = get_generated_sql_expected("arc_map_server_generate_sql_preamble.txt")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        map_server.db_client.exec_non_query(sql)
    except:
        assert False
