from requests import get
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_layer import ArcLayer
import pytest
from arc_query_builder import ArcQueryBuilder
from arc_set_data_loader import ArcSetDataLoader
from time import sleep

@pytest.fixture(autouse=True)
def arc_layer(url, folder, db_type):
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
    create_schema = sql_client.sql_generator_templates['create_schema'].format(schema=folder,
                                                                               schema_quoted=schema_quoted)
    sql_client.exec_non_query(create_schema, autocommit=True)
    arc_layer = ArcLayer(url, folder, sql_client)
    sql = sql_client.sql_generator_templates['create_stats_table']
    sql += sql_client.statement_terminator + sql_client.sql_generator_templates['create_error_table']
    sql += sql_client.statement_terminator + arc_layer.generate_sql_preamble()
    sql += sql_client.statement_terminator + arc_layer.generate_sql()
    sql += sql_client.statement_terminator + arc_layer.generate_sql_extra()

    try:
        arc_layer.db_client.exec_non_query(sql, autocommit=True)
    except:
        assert False

    return arc_layer


@pytest.mark.parametrize("url, folder, db_type", [
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik',
     'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik',
     'postgresql')
    ])
def test_arc_set_data_loader_init(arc_layer):

    loader = ArcSetDataLoader(arc_layer)

    assert loader.db_client is not None
    assert loader.arc_set == arc_layer


@pytest.mark.parametrize("url, folder, db_type", [
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik',
     'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'postgresql')
    ])
def test_arc_set_data_loader_load_stats(arc_layer):

    loader = ArcSetDataLoader(arc_layer)

    loader.load_stats()
    assert loader._ArcSetDataLoader__min_OID > -1
    assert loader._ArcSetDataLoader__max_OID > 0
    assert loader._ArcSetDataLoader__record_count > 0
    assert loader._ArcSetDataLoader__record_count >= \
           (loader._ArcSetDataLoader__max_OID - loader._ArcSetDataLoader__min_OID)
    assert len(loader.errors) == 0


@pytest.mark.parametrize("url, folder, db_type", [
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'mssql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'mysql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'sinav', 'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'klhk_en', 'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'publik',
     'postgresql'),
    ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'publik', 'postgresql'),
    ])
def test_arc_set_data_loader_load_data(arc_layer):
    loader = ArcSetDataLoader(arc_layer)

    truncate_table = arc_layer.db_client.sql_generator_templates['truncate_table']\
        .format(table_name=arc_layer.sql_full_table_name)
    arc_layer.db_client.exec_non_query(truncate_table)
    loader.load_data()
    # assert len(loader.errors) == 0
    assert loader.record_count == loader.loaded_record_count

    loader._ArcSetDataLoader__get_object_ids_from_db()
    assert len(loader._ArcSetDataLoader__loaded_OIDs) == loader.loaded_record_count

    select = arc_layer.db_client.sql_generator_templates['select_object_ids']\
        .format(table_name=arc_layer.sql_full_table_name, object_id_field_name=loader.object_id_field_name)
    results = arc_layer.db_client.exec_result_set_query(select) or ()
    assert len(results) == loader.loaded_record_count
    sleep(1)
    loader.load_data()
    # assert len(loader.errors) == 0
    assert loader.record_count == loader.loaded_record_count
    assert len(loader._ArcSetDataLoader__loaded_OIDs) == loader.loaded_record_count
