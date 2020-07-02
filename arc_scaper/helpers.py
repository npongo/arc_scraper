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
    if isinstance(json_list, dict):
        json_list = [v for k, v in json_list.items()]
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
    if json == "" or len(json['rings']) == 0:
        return "POLYGON EMPTY"
    if len(json.get('rings', [])) > 1:
        wtk_part = 'MULTIPOLYGON((({0})))'.format("),(".join([format_linestring(p) for p in json['rings'] if len(p) > 3]))
    else:
        wtk_part = 'POLYGON(({0}))'.format("),(".join([format_linestring(p) for p in json['rings'] if len(p) > 3]))

    if wtk_part in ['POLYGON(())', 'MULTIPOLYGON((()))']:
        wtk_part = "POLYGON EMPTY"
    return wtk_part


def esri_json_to_point(json):
    if json == "" or len(json) == 0:
        return "POINT EMPTY"
    wtk_part = 'POINT({0})'.format(format_point(json))
    return wtk_part


def esri_json_to_multi_point(json):
    if json == "":
        return "MULTIPOINT EMPTY"
    wtk_part = "MULTIPOINT({0})".format(format_multi_point(json))
    return wtk_part


def esri_json_to_linestring(json):
    if json == "" or len(json['rings']) == 0:
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

esri_geometry_to_empty_wtk = {
    'esriGeometryPoint': 'POINT EMPTY',
    'esriGeometryMultipoint': 'MULTIPOINT EMPTY',
    'esriGeometryPolyline': 'LINESTRING EMPTY',
    'esriGeometryPolygon': 'POLYGON EMPTY',
    'esriGeometryEnvelope': 'ENVELOPE EMPTY'
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


def sanitize_name(name, max_length=-63, underscore_leading_number=True,
                  force_lower_case=True,
                  replacement_dict={'': u"`~!@#$%^*()+=][{}\\|?><,/;:'\"",
                                    "_":  u".-& "} ):
    """
    sanitizes a name of special characters so that it can be used as a name in a databasing system
    :param name: string to be sanitized
    :param max_length: the maximum length of the sanitized name, negative numbers start from end
    :param underscore_leading_number: add an underscore in front of the name if it starts with a number
    :param force_lower_case: force the name to all lower case if true
    :param replacement_dict: a dictionary with value the character(s) to replace with the character(s) of the key
    :return: a sanitized string
    """
    for k, v in replacement_dict.items():
        for c in v:
             name = str(name).replace(c, k)

    if max_length < 0:
        name = name[max_length:]
    else:
        name = name[:max_length]

    if name[0] in "1234567890" and underscore_leading_number:
        name = f"_{name}"

    if force_lower_case:
        name = name.lower()

    return str(name)


def sanitize_and_quote_name(name, quote='[]', max_length=-63,
                            underscore_leading_number=True,
                            force_lower_case=False,
                            replacement_dict={'': u"`~!@#$%^*()+=][{}\\|?><,/;:'\"",
                                              "_":  u".-& "}):
    """
    sanitizes a name of special characters so that it can be used as a name in a databasing system
    :param name: string to be sanitized
    :param quote: character(s) to quote name with, can be two characters (start and end)
    :param max_length: the maximum length of the sanitized name, negative numbers start from end
    :param underscore_leading_number: add an underscore in front of the name if it starts with a number
    :param force_lower_case: force the name to all lower case if true
    :param replacement_dict: a dictionary with value the character(s) to replace with the character(s) of the key
    :return: a sanitized  and quoted string
    """
    quote_start = quote[0]
    quote_end = (quote + quote)[1]
    name = sanitize_name(name,
                         max_length=max_length,
                         force_lower_case=force_lower_case,
                         underscore_leading_number=underscore_leading_number,
                         replacement_dict=replacement_dict)
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
