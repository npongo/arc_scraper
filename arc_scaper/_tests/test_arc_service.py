from arc_service import ArcService
import requests
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
import pytest


@pytest.fixture(autouse=True)
def arc_service(monkeypatch, url, db_type, folder):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    # uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV'
    # folder = "sinav"
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

    return ArcService(url, folder, "<dumpy arc rest model>", sql_client)


@pytest.mark.parametrize("url, folder, db_type, expected", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mssql', 14),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mysql', 50),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mssql', 5)
                                                  ])
def test_arc_service_init(arc_service, expected):
    arm = arc_service

    assert len(arm.errors) == 0
    assert len(arm.arc_map_servers) == expected


@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'postgresql')
                                                  ])
def test_arc_service_generate_sql_preamble(db_type, arc_service):
    service = arc_service
    sql = service.generate_sql_preamble()

    save_test_to_file(f"arc_service_generate_sql_preamble_{db_type}.sql", sql)
    sql_expected = get_generated_sql_expected(f"arc_service_generate_sql_preamble_{db_type}.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql)
    except:
        assert False


@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'postgresql')
                                                  ])
def test_arc_service_generate_sql(db_type, arc_service):
    test_arc_service_generate_sql_preamble(db_type, arc_service)
    service = arc_service

    sql = service.generate_sql()

    save_test_to_file(f"arc_service_generate_sql_{db_type}.sql", sql)
    sql_expected = get_generated_sql_expected(f"arc_service_generate_sql_{db_type}.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql)
    except:
        assert False


@pytest.mark.parametrize("url, folder, db_type", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mssql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'mysql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV', 'SINAV', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN', 'KLHK_EN', 'postgresql'),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik', 'Publik', 'postgresql')
                                                  ])
def test_arc_service_generate_sql_extra(db_type, arc_service):
    test_arc_service_generate_sql(db_type, arc_service)
    service = arc_service
    sql = service.generate_sql_extra()

    save_test_to_file(f"arc_service_generate_sql_extra_{db_type}.sql", sql)
    sql_expected = get_generated_sql_expected(f"arc_service_generate_sql_extra_{db_type}.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql)
    except:
        assert False

