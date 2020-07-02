from requests import get
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_layer import ArcLayer
import pytest
from arc_query_builder import ArcQueryBuilder
from arc_set_data_loader import ArcSetDataLoader
from db_clients.mssql_db_client import SqlServerClient


@pytest.fixture(autouse=True)
def arc_layer(url, folder, db_type='mssql'):
    sql_client = get_db_conn(db_type)
    sql_client.db_conn['database'] = 'Indonesia_menlhk'
    return ArcLayer(url, folder, sql_client)


@pytest.mark.parametrize("url, folder", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik')])
def test_arc_set_data_loader_init(arc_layer):

    loader = ArcSetDataLoader(arc_layer)

    assert loader.db_client is not None
    assert loader.arc_set == arc_layer


@pytest.mark.parametrize("url, folder", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik')])
def test_arc_set_data_loader_load_stats(arc_layer):

    loader = ArcSetDataLoader(arc_layer)

    loader.load_stats()
    assert loader._ArcSetDataLoader__min_OID > -1
    assert loader._ArcSetDataLoader__max_OID > 0
    assert loader._ArcSetDataLoader__record_count > 0
    assert loader._ArcSetDataLoader__record_count >= \
           (loader._ArcSetDataLoader__max_OID - loader._ArcSetDataLoader__min_OID)
    assert len(loader.errors) == 0


@pytest.mark.parametrize("url, folder", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'SINAV'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'KLHK_EN'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/Def_2017_2018_Publik/MapServer/0', 'Publik'),
                                         ('http://geoportal.menlhk.go.id/arcgis/rest/services/Publik/IUPHHK_HT_Publik/MapServer/0', 'Publik')])
def test_arc_set_data_loader_load_data(arc_layer):
    loader = ArcSetDataLoader(arc_layer)

    truncate_table = arc_layer.db_client.sql_generator_templates['truncate_table']\
        .format(table_name=arc_layer.sql_table_name)
    arc_layer.db_client.exec_non_query(truncate_table)
    loader.load_data()
    assert len(loader.errors) == 0
    assert loader.record_count == loader.loaded_record_count

    loader._ArcSetDataLoader__get_object_ids_from_db()
    assert len(loader._ArcSetDataLoader__loaded_OIDs) == loader.loaded_record_count

    select = arc_layer.db_client.sql_generator_templates['select_object_ids']\
        .format(table_name=arc_layer.sql_table_name, object_id_field_name=loader.object_id_field_name)
    results = arc_layer.db_client.exec_result_set_query(select) or ()
    assert len(results) == loader.loaded_record_count

    loader.load_data()
    assert len(loader.errors) == 0
    assert loader.record_count == loader.loaded_record_count
    assert len(loader._ArcSetDataLoader__loaded_OIDs) == loader.loaded_record_count
