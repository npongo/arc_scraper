import pickle
from requests import get
from urllib.parse import urlparse


def dump_url():
    base_dir = "C:\\Users\\npongo\\Dropbox\\PythonProjects\\ArcMapService\\arc_scaper\\_tests\\responses"
    base_url = "http://geoportal.menlhk.go.id/arcgis/rest/"

    url1 = f"{base_url}?f=json"
    response = get(url1)
    if response.ok:
        f_name = f"{base_dir}\\{urlparse(base_url).netloc.replace('.','_')}.json"
        pickle.dump(response, open(f_name, 'wb'))
        json1 = response.json()
        for f in json1['folders']:
            if f != "SINAV":
                continue
            url2 = "{0}services/{1}/?f=json".format(base_url, f)
            response = get(url2)
            if response.ok:
                f_name = f"{base_dir}\\{urlparse(base_url).netloc.replace('.', '_')}_{f}.json"
                pickle.dump(response, open(f_name, 'wb'))
                json2 = response.json()
                if 'services' not in json2:
                    continue
                for s in [s for s in json2['services'] if s['type'] == 'MapServer']:
                    name = s['name'].split("/")[-1]
                    url3 = f"{base_url}services/{f}/{name}/MapServer/?f=json"
                    response = get(url3)
                    if response.ok:
                        f_name = f"{base_dir}\\{urlparse(base_url).netloc.replace('.', '_')}_{f}_{name}.json"
                        pickle.dump(response, open(f_name, 'wb'))
                        json3 = response.json()
                        if 'layers' not in json3:
                            continue
                        # for l in json3['layers']:
                        #     url4 = "{0}/{1}?f=json".format(url3.replace('/?f=json', ''), l['id'])
                        #     response = get(url4)
                        #     if response.ok:
                        #         f_name = f"{base_dir}\\{urlparse(base_url).netloc.replace('.', '_')}_{f}_{name}_{l['id']}.json"
                        #         pickle.dump(response, open(f_name, 'wb'))

                        for l in json3['tables']:
                            url4 = "{0}/{1}?f=json".format(url3.replace('/?f=json', ''), l['id'])
                            response = get(url4)
                            if response.ok:
                                f_name = f"{base_dir}\\{urlparse(base_url).netloc.replace('.', '_')}_{f}_{name}_{l['id']}.json"
                                pickle.dump(response, open(f_name, 'wb'))
