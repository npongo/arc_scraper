from db_clients.mssql_db_client import SqlServerClient
import pytest
from datetime import datetime
from _tests.secrets import db_conns

@pytest.fixture()
def sql_client():
    sql_conn = SqlServerClient(db_conns['mssql'])
    return sql_conn

@pytest.fixture()
def init_table(sql_client):
    d_sql = "if object_id('test_exec_non_query') is not null drop table test_exec_non_query"
    sql_client.exec_non_query(d_sql)
    c_sql = "create table test_exec_non_query(id int not null primary key, test varchar(64) NULL)"
    sql_client.exec_non_query(c_sql)
    return True


@pytest.fixture()
def init_table_with_data(sql_client, init_table):
    i_sql = "INSERT INTO test_exec_non_query VALUES(1,'TEST1'),(2,'TEST2')"
    sql_client.exec_non_query(i_sql)
    return True


@pytest.mark.parametrize("sql, expected", [('SELECT 1', 1),
                                         ("SELECT 'MY_TEST'", 'MY_TEST'),
                                         ("SELECT CAST('2020-01-01' AS Datetime)", datetime(2020, 1, 1)),
                                         ("SELECT CASE WHEN COUNT(*)>0 THEN 1 ELSE 0 END FROM sys.tables", 1)])
def test_exec_scalar_query(sql_client, init_table_with_data, sql, expected):
    result = sql_client.exec_scalar_query(sql)
    assert result == expected


@pytest.mark.parametrize("sql, sql_expected, expected", [("if object_id('test_exec_non_query') is not null drop table test_exec_non_query",
                                                          "SELECT 1", 1),
                                                         ('create table test_exec_non_query(id int not null primary key, test varchar(64) NULL)',
                                                          "select 1 from sys.tables where name = 'test_exec_non_query'", 1),
                                                         ("INSERT INTO test_exec_non_query VALUES(1,'TEST1'),(2,'TEST2')",
                                                          'SELECT COUNT(*) FROM test_exec_non_query', 2)])
def test_exec_non_query(sql_client, sql, sql_expected, expected):
    sql_client.exec_non_query(sql)
    result = sql_client.exec_scalar_query(sql_expected)
    assert result == expected


@pytest.mark.parametrize("sql, expected", [("select id from test_exec_non_query", [(1,), (2,)]),
                                           ("select test from test_exec_non_query", [('TEST1',), ('TEST2',)]),
                                           ("select * from test_exec_non_query", [(1, 'TEST1'), (2, 'TEST2')])])
def test_exec_result_set_query(sql_client, sql, expected, init_table_with_data):
    result = sql_client.exec_result_set_query(sql)
    assert result == expected


@pytest.mark.parametrize("data", [[(1, 'test1'), (2, 'test2'), (3, 'test4')],
                                  [(4, 'test4'), (5, 'test5')],
                                  [(6, 'test6'), (7, 'test7'), (8, 'test8'), (9, 'test9')]])
def test_run_bulk_insert(sql_client, data, init_table):
    def formatter(row):
        return "({})".format(",".join(["'{}'".format(r) for r in row]))

    insert_template = "insert into test_exec_non_query(id, test)values{0}"
    k = sql_client.run_bulk_insert(insert_template, data, formatter, batch=2)
    assert k == len(data)


@pytest.mark.parametrize("name, expected", [('1', '[1]'), ('name', '[name]'), ('[name]', '[name]')])
def test_quote_name(sql_client, name, expected):
    result = sql_client.quote_name(name)
    assert result == expected


@pytest.mark.parametrize("name, expected", [('1?.*', '[_1_]'), ('na[]me', '[name]'), ('[na*&(*))_me]', '[na_me]')])
def test_sanitize_and_quote_name(sql_client, name, expected):
    result = sql_client.sanitize_and_quote_name(name)
    assert result == expected

@pytest.mark.parametrize("name", ["table_name", "null_string", "esriFieldTypeOID", "esriFieldTypeString",
                                  "esriFieldTypeDate", "unique_field", "unique_constraint",
                                  "primary_constraint", "create_spatial_index", "create_index",
                                  "foreign_key_constraint", "create_schema", "rangeValue", "codedValue",
                                  "select_object_ids", "data_insert", "data_row_insert", "spatial_data_insert",
                                  "null_spatial_data_insert", "create_database", "drop_if_exists_create_table",
                                  "create_code_table_with_data", "code_table_fields", "insert_code_table_row",
                                  "code_table_foreign_key", "truncate_table",
                                  "insert_stats", "create_stats_table"])
def test_sql_generator_templates(sql_client, name):
    assert name in sql_client.sql_generator_templates