from requests import get
from db_clients.mssql_db_client import SqlServerClient
from _tests.mock_helper import mock_get_return, get_db_conn, get_generated_sql_expected, save_test_to_file
from arc_layer import ArcLayer
import pytest
from arc_query_builder import ArcQueryBuilder


@pytest.fixture(autouse=True)
def arc_layer(url, folder, db_type):
    # uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0'
    # uri = 'http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0'
    # folder = "SINAV"
    sql_client = get_db_conn(db_type)
    return ArcLayer(url, folder, sql_client)

@pytest.mark.parametrize("url, folder, db_type, expected", [('http://geoportal.menlhk.go.id/arcgis/rest/services/SINAV/Usulan_IPHPS/MapServer/0', 'test', 'mssql', 2),
                                                  ('http://geoportal.menlhk.go.id/arcgis/rest/services/KLHK_EN/IUPHHK_RE/MapServer/0', 'test', 'mysql', 5)
                                                  ])
def test_query_builder_init(arc_layer, url, expected):
    query = ArcQueryBuilder(arc_layer)
    query.return_ids_only = True
    query.return_geometry = False
    assert str(query) == f"{url}/query?f=json&where=1%3D1&returnGeometry=False&maxAllowableOffset=0&geometryPrecision=12&outSR=4326&returnIdsOnly=True&returnCountOnly=False&returnExtentOnly=False&returnZ=True&returnM=True&returnDistinctValues=False&returnTrueCurves=False"

    resp = get(query)
    if resp.ok:
        assert resp.json().get('objectIds', None) is not None
    else:
        assert False

    query.return_ids_only = False
    #query.return_geometry = True
    query.object_ids = [1, 2, 3, 4, 5]
    resp = get(query)
    if resp.ok:
        assert len(resp.json().get('features', [])) == expected
    else:
        assert False
    query.object_ids = None
    query.where = f'OBJECTID<={expected}'
    resp = get(query)
    if resp.ok:
        assert len(resp.json().get('features', [])) == expected
    else:
        assert False