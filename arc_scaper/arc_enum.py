from enum import Enum, auto
from datetime import datetime, timedelta


esriTypes_to_sql = {
    "esriFieldTypeSmallInteger": "smallint",
    "esriFieldTypeSingle": "real",
    "esriFieldTypeString": "varchar({0})",
    "esriFieldTypeDate": "bigint",  # datetime",
    "esriFieldTypeGeometry": "geometry",
    "esriFieldTypeOID": "int",
    "esriFieldTypeBlob": "varbinary({0})",
    "esriFieldTypeGlobalID": "uniqueidentifier",
    "esriFieldTypeRaster": "varbinary({0})",
    "esriFieldTypeGUID": "uniqueidentifier",
    "esriFieldTypeXML": "XML",
    "esriFieldTypeDouble": "float",
    "esriFieldTypeInteger": "int"
}


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class AutoLowerName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class ArcSpatialRel(AutoName):
    """
    represents the options for the arc spatial relationship
    """
    esriSpatialRelIntersects = auto()
    esriSpatialRelContains = auto()
    esriSpatialRelCrosses = auto()
    esriSpatialRelEnvelopeIntersects = auto()
    esriSpatialRelIndexIntersects = auto()
    esriSpatialRelOverlaps = auto()
    esriSpatialRelTouches = auto()
    esriSpatialRelWithin = auto()
    esriSpatialRelRelation = auto()


class ArcGeometryType(AutoName):
    """
    represents the options for the arc geometry types
    """
    esriGeometryPoint = auto()
    esriGeometryMultipoint = auto()
    esriGeometryPolyline = auto()
    esriGeometryPolygon = auto()
    esriGeometryEnvelope = auto()


class ArcFormat(AutoLowerName):
    """
    represents the options for the arc format
    """
    HTML = auto()
    JSON = auto()
    GEOJSON = auto()
    KMZ = auto()
    PBF = auto()


class ArcUnit(AutoName):
    """
    represents the options for the arc unit
    """

    esriSRUnit_Meter = auto()
    esriSRUnit_StatuteMile = auto()
    esriSRUnit_Foot = auto()
    esriSRUnit_Kilometer = auto()
    esriSRUnit_NauticalMile = auto()
    esriSRUnit_USNauticalMile = auto()


class ArcStatisticType(AutoLowerName):
    """
    represents the options for the arc statistics
    """
    COUNT = auto()
    SUM = auto()
    MIN = auto()
    MAX = auto()
    AVG = auto()
    STDDEV = auto()
    VAR = auto()


class ArcTime:
    """
    string representation of time filter in an arc service
    """
    def __init__(self, time=None, start_time=None, end_time=None):
        super().__init__()
        if not isinstance(time, datetime) and time is not None:
            raise Exception("Time parameter must be a datetime or None")
        if not isinstance(start_time, datetime) and start_time is not None:
            raise Exception("Start time parameter must be a datetime or None")
        if not isinstance(end_time, datetime) and end_time is not None:
            raise Exception("End time parameter must be a datetime or None")
        self.__time = time
        self.__start_time = start_time
        self.__end_time = end_time
        self.value = self.get_arc_time()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value
        self.get_arc_time()

    def fluent_time(self, value):
        self.__time = value
        self.get_arc_time()
        return self

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value
        self.get_arc_time()

    def fluent_start_time(self, value):
        self.__start_time = value
        self.get_arc_time()
        return self

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value
        self.get_arc_time()

    def fluent_end_time(self, value):
        self.__end_time = value
        self.get_arc_time()
        return self

    def get_arc_time(self):
        if self.__time is None and self.__start_time is None and self.__end_time is None:
            raise Exception("Atleast one time value must be specificed (Time, StartTime, EndTime equal null)!")

        unix_time = datetime(1970, 1, 1)

        if self.__time is not None:
            delta = self.__time - unix_time
            self.value = str(round(delta.total_seconds()*1000000 + delta.microseconds * 0.001))
        else:
            if (self.start_time or self.end_time) > (self.end_time or self.start_time):
                raise Exception("StartTime greater or equal to EndTime!")

            delta_start = self.start_time - unix_time
            delta_end = self.end_time - unix_time
            self.value = "{0}, {1}".format(
                         str(round(delta_start.total_seconds()*1000000 + delta_start.microseconds * 0.001)),
                         str(round(delta_end.total_seconds()*1000000 + delta_end.microseconds * 0.001)))

        return self.value

    def __repr__(self):
        return self.get_arc_time()

    def __str__(self):
        return self.get_arc_time()


class ArcOutStatistic(str):
    """
    representation of a arc out statistic for the REST API
    """

    def __init__(self, statistic_type, on_field, out_field):
        if not isinstance(statistic_type, ArcStatisticType):
            raise Exception("statistic type is not of class ArcStatisticType")
        self.__statistic_type = statistic_type
        self.__on_field = on_field
        self.__out_field = out_field
        self.value = self.get_query_value()

    @property
    def statistic_type(self):
        return self.__statistic_type

    @statistic_type.setter
    def statistic_type(self, value):
        self.__statistic_type = value
        self.get_query_value()

    def statistic_type(self, value):
        self.__statistic_type = value
        self.get_query_value()
        return self

    @property
    def on_field(self):
        return self.__on_field

    @on_field.setter
    def on_field(self, value):
        self.__on_field = value
        self.get_query_value()

    def on_field(self, value):
        self.__on_field = value
        self.get_query_value()
        return self

    @property
    def out_field(self):
        return self.__out_field

    @out_field.setter
    def out_field(self, value):
        self.__out_field = value
        self.get_query_value()

    def out_field(self, value):
        self.__out_field = value
        self.get_query_value()
        return self

    def get_query_value(self):
        """

        :return:
        """
        self.value = '{{ "statisticType": "{0}", "onStatisticField": "{1}", "outStatisticFieldName": "{2}" }}'\
            .format(self.__statistic_type.value, self.__on_field, self.__out_field)
        return self.value

    def __repr__(self):
        return self.get_query_value()

    def __str__(self):
        return self.get_query_value()

