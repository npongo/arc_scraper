from arc_rest_model import ArcRestModel
import requests
from os import path
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
import pytest


@pytest.fixture(autouse=True)
def arc_rest_model(monkeypatch, db_type):
    monkeypatch.setattr(requests, 'get', mock_get_return)
    uri = "http://geoportal.menlhk.go.id/arcgis/rest"
    sql_client = get_db_conn(db_type)
    database = sql_client.db_conn['database']
    sql_client.db_conn['database'] = sql_client.sql_generator_options['master_database']
    drop_database = sql_client.sql_generator_templates['drop_database'].format(database=database)
    sql_client.exec_non_query(drop_database, autocommit=True)
    create_database = sql_client.sql_generator_templates['create_database'].format(database=database)
    sql_client.exec_non_query(create_database, autocommit=True)
    sql_client.db_conn['database'] = database
    return ArcRestModel(uri, database, sql_client)


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_init(arc_rest_model):
    arm = arc_rest_model

    for e in arm.errors:
        print(e)
    assert len(arm.errors) == 24
    assert len(arm.arc_services) == 9

@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_generate_sql(arc_rest_model):
    service = arc_rest_model
    sql = service.generate_sql()

    save_test_to_file(f"{arc_rest_model.db_client.name}_arc_service_generate_sql.sql", sql)
    sql_expected = get_generated_sql_expected(f"{arc_rest_model.db_client.name}_arc_service_generate_sql.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql)
    except:
        assert False


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_generate_sql_extra(arc_rest_model):
    service = arc_rest_model
    sql = service.generate_sql_extra()

    save_test_to_file(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_extra.sql", sql)
    sql_expected = get_generated_sql_expected(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_extra.sql")

    assert sql.replace("\n", '').replace("\r", "").replace("\t", '').strip() \
           == sql_expected.replace("\n", '').replace("\r", "").replace("\t", '').strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql)
    except:
        assert False


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_arc_rest_model_generate_sql_preamble(arc_rest_model):
    service = arc_rest_model
    sql = service.generate_sql_preamble()

    save_test_to_file(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_preamble.sql", sql)
    sql_expected = get_generated_sql_expected(f"{arc_rest_model.db_client.name}_arc_service_generate_sql_preamble.sql")

    assert sql.strip() == sql_expected.strip()

    # sql_parse = f"SET PARSEONLY ON;\r\nGO\r\n{sql}SET PARSEONLY OFF;"
    try:
        service.db_client.exec_non_query(sql)
    except:
        assert False


@pytest.mark.parametrize("db_type, file", [('mssql', "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\MSSql_Script.sql"),
                                           ('mysql', "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\MySql_Script.sql"),
                                           ('postgresql', "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\test_output\\PostgreSql_Script.sql")])
def test_save_sql_script(arc_rest_model, file):
    arm = arc_rest_model
    arm.save_sql_script(file)
    assert path.isfile(file)


@pytest.mark.parametrize("db_type", ['mssql', 'mysql', 'postgresql'])
def test_run_sql_script(db_type, arc_rest_model):
    arm = arc_rest_model
    try:
        arm.run_sql()
    except:
        assert False

    sql = "select count(*) from information_schema.tables \
           where table_schema in('arc','klhk','klhk_en','sinav','test','publik','other')"
    result = arc_rest_model.db_client.exec_scalar_query(sql)
    assert result >= 153
