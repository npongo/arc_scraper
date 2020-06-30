import re
from uuid import UUID
from sys import exc_info
from os.path import split
from collections import defaultdict


def validate_url(url):
    """
    validates that a url is well formed.
    :param url: url to validate
    :return: bool, true if url is well formed
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def format_point(json_list):
    wtk_part = " ".join([str(p or '0') for p in json_list])
    return wtk_part


def format_multi_point(json_list_list):
    wtk_part = "({0})".format("),(".join([format_point(p) for p in json_list_list]))
    return wtk_part


def format_linestring(json_list_list):
    wtk_part = ",".join([format_point(p) for p in json_list_list])
    return wtk_part


def format_linestrings(json_list_list_list):
    wtk_part = "({})".format("),(".join([format_linestring(ls) for ls in json_list_list_list]))
    return wtk_part


def esri_json_to_polygon(json):
    if json == "":
        return "POLYGON EMPTY"
    if len(json.get('rings', [])) > 1:
        wtk_part = 'MULTIPOLYGON((({0})))'.format("),(".join([format_linestring(p) for p in json['rings']]))
    else:
        wtk_part = 'POLYGON(({0}))'.format("),(".join([format_linestring(p) for p in json['rings']]))
    return wtk_part


def esri_json_to_point(json):
    if json == "":
        return "POINT EMPTY"
    wtk_part = 'POINT({0})'.format(format_point(json))
    return wtk_part


def esri_json_to_multi_point(json):
    if json == "":
        return "MULTIPOINT EMPTY"
    wtk_part = "MULTIPOINT({0})".format(format_multi_point(json))
    return wtk_part


def esri_json_to_linestring(json):
    if json == "":
        return "LINESTRING EMPTY"
    if len(json) > 1:
        wtk_part = "MULTILINESTRING(({0}))".format(format_linestrings(json))
    else:
        wtk_part = "LINESTRING({0})".format(format_linestrings(json))
    return wtk_part


# TODO: IMPLEMENT
def esri_json_to_envelope(json):
    return '<not implemented> ' + json


def default():
    return esri_json_to_point

json_to_wkt = {
    'esriGeometryPoint': esri_json_to_point,
    'esriGeometryMultipoint': esri_json_to_multi_point,
    'esriGeometryPolyline': esri_json_to_linestring,
    'esriGeometryPolygon': esri_json_to_polygon,
    'esriGeometryEnvelope': esri_json_to_envelope
    }


esriType_to_dot_net = {"esriFieldTypeSmallInteger": type(int),
                       "esriFieldTypeSingle": type(float),
                       "esriFieldTypeString": type(str),
                       "esriFieldTypeDate": type(int),
                       "esriFieldTypeGeometry": type(str),
                       "esriFieldTypeOID": type(int),
                       "esriFieldTypeBlob": type(bytearray),
                       "esriFieldTypeGlobalID": type(UUID),
                       "esriFieldTypeRaster": type(bytearray),
                       "esriFieldTypeGUID": type(UUID),
                       "esriFieldTypeXML": type(str),
                       "esriFieldTypeDouble": type(float),
                       "esriFieldTypeInteger": type(int)}


def sanitize_name(name, max_length=63):
    """
    sanitizes a name of special characters so that it can be used as a name in a databasing system
    :param name: string to be sanitized
    :return:
    """
    for c in u"`~!@#$%^*()+=][{}\|?><,/;:'\"":
         name = str(name).replace(c, "")

    for c in u".-& ":
         name = str(name).replace(c, "_")

    if name[0] in "1234567890":
        name = f"_{name}"

    return str(name)


def sanitize_and_quote_name(name, quote='[]'):
    """
    sanitizes a name of special characters so that it can be used as a name in a databasing system
    :param name: string to be sanitized
    :param quote: character(s) to quote name with, can be two characters (start and end)
    :return:
    """
    quote_start = quote[0]
    quote_end = (quote + quote)[1]
    name = sanitize_name(name)
    name = name.replace(quote_start, "")
    name = name.replace(quote_end, "")
    return f"{quote_start}{name}{quote_end}"


def exception_logging(e, persist=print):
    try:
        exc_type, exc_obj, exc_tb = exc_info()
        f_name = ""
        line_no = ""
        if exc_tb is not None:
            f_name = split(exc_tb.tb_frame.f_code.co_filename)[1]
            line_no = exc_tb.tb_lineno
        persist(e, exc_type, f_name, line_no)
    except:
        persist(e)
