from requests import get
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, db_conn, get_generated_sql_expected, save_test_to_file
from arc_layer import ArcLayer
import pytest
from arc_query_builder import ArcQueryBuilder


@pytest.fixture(autouse=True)
def arc_layer(autouse=True):
    uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0'
    uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0'
    folder = "SINAV"
    sql_conn = SqlServerClient(db_conn)
    return ArcLayer(uri, folder, sql_conn)


def test_query_builder_init(arc_layer):
    query = ArcQueryBuilder(arc_layer)

    assert str(query) == "http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0/query?f=json&where=1%3D1&returnGeometry=True&outSR=4326&returnIdsOnly=False&returnCountOnly=False&returnExtentOnly=False&returnZ=True&returnM=True&returnDistinctValues=False&returnTrueCurves=True"

    resp = get(query)
    if resp.ok:
        assert resp.json().get('features', None) is not None
    else:
        assert False

    query.object_ids = [1, 2, 3, 4, 5]
    resp = get(query)
    if resp.ok:
        assert len(resp.json().get('features', [])) == 5
    else:
        assert False
    query.object_ids = None
    query.where = 'OBJECTID<11'
    resp = get(query)
    if resp.ok:
        assert len(resp.json().get('features', [])) == 10
    else:
        assert False