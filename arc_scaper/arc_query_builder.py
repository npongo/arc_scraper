from sys import exc_info
from os.path import split
from urllib.parse import quote

class ArcQueryBuilder(str):
    """
    this class is a fluent representation of the arc map server query syntax
    """
    # TODO: add type checking on bools
    def __init__(self, arc_set):
        super().__init__()
        self.__arc_set = arc_set
        self.__object_ids = list()
        self.__out_fields = list()
        self.__order_by_fields = list()
        self.__out_statistics = list()
        self.__group_by_fields_statistics = list()
        self.__range_values = list()
        self.__parameter_values = list()
        # instance variables
        self.__format = "json"
        self.__text = None
        self.__geometry = None
        self.__geometry_type = None
        self.__in_SR = None
        self.__spatial_rel = None
        self.__relation_param = []
        self.__where = "1=1"
        self.__object_ids = []
        self.__time = None
        self.__distance = None
        self.__units = None
        self.__out_fields = []
        self.__return_geometry = True
        self.__max_allowable_offset = 0
        self.__geometry_precision = 12
        self.__out_SR = 4326
        self.__return_ids_only = False
        self.__return_count_only = False
        self.__return_extent_only = False
        self.__order_by_fields = []
        self.__out_statistics = []
        self.__group_by_fields_statistics = []
        self.__return_Z = True
        self.__return_M = True
        self.__gdb_version = None
        self.__return_distinct_values = False
        self.__return_true_curves = False  # currently not supported in parser
        self.__result_offset = None
        self.__result_record_count = None
        self.__datum_transformation = None
        self.__parameter_values = []
        self.__historic_moment = None
        self.value = self.get_query_string()

    @property
    def fields(self):
        return self.__arc_set.fields

    @property
    def arc_set(self):
        return self.__arc_set

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, value):
        self.__format = value
        self.get_query_string()

    def fluent_format(self, value):
        self.__format = value
        self.get_query_string()
        return self

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.get_query_string()

    def fluent_text(self, value):
        self.__text = value
        self.get_query_string()
        return self

    @property
    def geometry(self):
        return self.__geometry

    @geometry.setter
    def geometry(self, value):
        self.__geometry = value
        self.get_query_string()

    def fluent_geometry(self, value):
        self.__geometry = value
        self.get_query_string()
        return self

    @property
    def geometry_type(self):
        return self.__geometry_type

    @geometry_type.setter
    def geometry_type(self, value):
        self.__geometry_type = value
        self.get_query_string()

    def fluent_geometry_type(self, value):
        self.__geometry_type = value
        self.get_query_string()
        return self

    @property
    def in_SR(self):
        return self.__in_SR

    @in_SR.setter
    def in_SR(self, value):
        self.__in_SR = value
        self.get_query_string()

    def fluent_in_SR(self, value):
        self.__in_SR = value
        self.get_query_string()
        return self

    @property
    def spatial_rel(self):
        return self.__spatial_rel

    @spatial_rel.setter
    def spatial_rel(self, value):
        self.__spatial_rel = value
        self.get_query_string()

    def fluent_spatial_rel(self, value):
        self.__spatial_rel = value
        self.get_query_string()
        return self

    @property
    def relation_param(self):
        return self.__relation_param

    @relation_param.setter
    def relation_param(self, value):
        if value is None:
            value = []
        self.__relation_param = value
        self.get_query_string()

    def fluent_relation_param(self, value):
        if value is None:
            value = []
        self.__relation_param = value
        self.get_query_string()
        return self

    @property
    def where(self):
        return self.__where

    @where.setter
    def where(self, value):
        self.__where = value
        self.get_query_string()

    def fluent_where(self, value):
        self.__where = value
        self.get_query_string()
        return self

    @property
    def object_ids(self):
        return self.__object_ids

    @object_ids.setter
    def object_ids(self, value):
        if value is None:
            value = []
        self.__object_ids = value
        self.get_query_string()

    def fluent_object_ids(self, value):
        if value is None:
            value = []
        self.__object_ids = value
        self.get_query_string()
        return self

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value
        self.get_query_string()

    def fluent_time(self, value):
        self.__time = value
        self.get_query_string()
        return self

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value
        self.get_query_string()

    def fluent_distance(self, value):
        self.__distance = value
        self.get_query_string()
        return self

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, value):
        self.__units = value
        self.get_query_string()

    def fluent_units(self, value):
        self.__units = value
        self.get_query_string()
        return self

    @property
    def out_fields(self):
        return self.__out_fields

    @out_fields.setter
    def out_fields(self, value):
        if value is None:
            value = []
        self.__out_fields = value
        self.get_query_string()

    def fluent_out_fields(self, value):
        if value is None:
            value = []
        self.__out_fields = value
        self.get_query_string()
        return self

    @property
    def return_geometry(self):
        return self.__return_geometry

    @return_geometry.setter
    def return_geometry(self, value):
        self.__return_geometry = value
        self.get_query_string()

    def fluent_return_geometry(self, value):
        self.__return_geometry = value
        self.get_query_string()
        return self

    @property
    def max_allowable_offset(self):
        return self.__max_allowable_offset

    @max_allowable_offset.setter
    def max_allowable_offset(self, value):
        self.__max_allowable_offset = value
        self.get_query_string()

    def fluent_max_allowable_offset(self, value):
        self.__max_allowable_offset = value
        self.get_query_string()
        return self

    @property
    def geometry_precision(self):
        return self.__geometry_precision

    @geometry_precision.setter
    def geometry_precision(self, value):
        self.__geometry_precision = value
        self.get_query_string()

    def fluent_geometry_precision(self, value):
        self.__geometry_precision = value
        self.get_query_string()
        return self

    @property
    def out_SR(self):
        return self.__out_SR

    @out_SR.setter
    def out_SR(self, value):
        self.__out_SR = value
        self.get_query_string()

    def fluent_out_SR(self, value):
        self.__out_SR = value
        self.get_query_string()
        return self

    @property
    def return_ids_only(self):
        return self.__return_ids_only

    @return_ids_only.setter
    def return_ids_only(self, value):
        self.__return_ids_only = value
        self.get_query_string()

    def fluent_return_ids_only(self, value):
        self.__return_ids_only = value
        self.get_query_string()
        return self

    @property
    def return_count_only(self):
        return self.__return_count_only

    @return_count_only.setter
    def return_count_only(self, value):
        self.__return_count_only = value
        self.get_query_string()

    def fluent_return_count_only(self, value):
        self.__return_count_only = value
        self.get_query_string()
        return self

    @property
    def return_extent_only(self):
        return self.__return_extent_only

    @return_extent_only.setter
    def return_extent_only(self, value):
        self.__return_extent_only = value
        self.get_query_string()

    def fluent_return_extent_only(self, value):
        self.__return_extent_only = value
        self.get_query_string()
        return self

    @property
    def order_by_fields(self):
        return self.__order_by_fields

    @order_by_fields.setter
    def order_by_fields(self, value):
        if value is None:
            value = []
        self.__order_by_fields = value
        self.get_query_string()

    def fluent_order_by_fields(self, value):
        if value is None:
            value = []
        self.__order_by_fields = value
        self.get_query_string()
        return self

    @property
    def out_statistics(self):
        return self.__out_statistics

    @out_statistics.setter
    def out_statistics(self, value):
        if value is None:
            value = []
        self.__out_statistics = value
        self.get_query_string()

    def fluent_out_statistics(self, value):
        if value is None:
            value = []
        self.__out_statistics = value
        self.get_query_string()
        return self

    @property
    def group_by_fields_statistics(self):
        return self.__group_by_fields_statistics

    @group_by_fields_statistics.setter
    def group_by_fields_statistics(self, value):
        if value is None:
            value = []
        self.__group_by_fields_statistics = value
        self.get_query_string()

    def fluent_group_by_fields_statistics(self, value):
        if value is None:
            value = []
        self.__group_by_fields_statistics = value
        self.get_query_string()
        return self

    @property
    def return_Z(self):
        return self.__return_Z

    @return_Z.setter
    def return_Z(self, value):
        self.__return_Z = value
        self.get_query_string()

    def fluent_return_Z(self, value):
        self.__return_Z = value
        self.get_query_string()
        return self

    @property
    def return_M(self):
        return self.__return_M

    @return_M.setter
    def return_M(self, value):
        self.__return_M = value
        self.get_query_string()

    def fluent_return_M(self, value):
        self.__return_M = value
        self.get_query_string()
        return self

    @property
    def gdb_version(self):
        return self.__gdb_version

    @gdb_version.setter
    def gdb_version(self, value):
        self.__gdb_version = value
        self.get_query_string()

    def fluent_gdb_version(self, value):
        self.__gdb_version = value
        self.get_query_string()
        return self

    @property
    def return_distinct_values(self):
        return self.__return_distinct_values

    @return_distinct_values.setter
    def return_distinct_values(self, value):
        self.__return_distinct_values = value
        self.get_query_string()

    def fluent_return_distinct_values(self, value):
        self.__return_distinct_values = value
        self.get_query_string()
        return self

    @property
    def return_true_curves(self):
        return self.__return_true_curves

    @return_true_curves.setter
    def return_true_curves(self, value):
        self.__return_true_curves = value
        self.get_query_string()

    def fluent_return_true_curves(self, value):
        self.__return_true_curves = value
        self.get_query_string()
        return self

    @property
    def result_offset(self):
        return self.__result_offset

    @result_offset.setter
    def result_offset(self, value):
        self.__result_offset = value
        self.get_query_string()

    def fluent_result_offset(self, value):
        self.__result_offset = value
        self.get_query_string()
        return self

    @property
    def result_record_count(self):
        return self.__result_record_count

    @result_record_count.setter
    def result_record_count(self, value):
        self.__result_record_count = value
        self.get_query_string()

    def fluent_result_record_count(self, value):
        self.__result_record_count = value
        self.get_query_string()
        return self

    @property
    def datum_transformation(self):
        return self.__datum_transformation

    @datum_transformation.setter
    def datum_transformation(self, value):
        self.__datum_transformation = value
        self.get_query_string()

    def fluent_datum_transformation(self, value):
        self.__datum_transformation = value
        self.get_query_string()
        return self

    @property
    def range_values(self):
        return self.__range_values

    @range_values.setter
    def range_values(self, value):
        self.__range_values = value
        self.get_query_string()

    def fluent_range_values(self, value):
        self.__range_values = value
        self.get_query_string()
        return self

    @property
    def parameter_values(self):
        return self.__parameter_values

    @parameter_values.setter
    def parameter_values(self, value):
        if value is None:
            value = []
        self.__parameter_values = value
        self.get_query_string()

    def fluent_parameter_values(self, value):
        if value is None:
            value = []
        self.__parameter_values = value
        self.get_query_string()
        return self

    @property
    def historic_moment(self):
        return self.__historic_moment

    @historic_moment.setter
    def historic_moment(self, value):
        self.__historic_moment = value
        self.get_query_string()

    def fluent_historic_moment(self, value):
        self.__historic_moment = value
        self.get_query_string()
        return self

    def get_query_string(self):
        """

        :return:
        """
        try:
            query = "{0}/query?".format((self.__arc_set).uri)

            if len(self.__object_ids) == 1:
                query = "{0}/{1}/query?".format((self.__arc_set).uri, self.__object_ids[0])

            if self.__format is not None:
                query += "f={0}".format(self.__format)
            else:
                query += "f=html"

            if self.__text is not None:
                query += "&text={0}".format(quote(self.__text))

            if self.__geometry is not None:
                query += "&geometry={0}".format(quote(self.__geometry))

            if self.__geometry_type is not None:
                query += "&geometryType={0}".format(self.__geometry_type)

            if self.__in_SR is not None:
                query += "&inSR={0}".format(self.__in_SR)

            if self.__spatial_rel is not None:
                query += "&spatialRel={0}".format(self.__spatial_rel)

            if len(self.__relation_param) > 0:
                query += "&relationParam={0}".format(quote(self.__relation_param))

            if self.__where is not None and len(self.__object_ids) != 1:
                query += "&where={0}".format(quote(self.__where))

            if len(self.__object_ids) > 1:
                query += "&objectIds={0}".format(quote(",".join([str(i) for i in self.__object_ids])))

            # TODO: handling of arc time formating
            if self.__time is not None:
                query += "&time={0}".format(self.__time.get_arc_time())

            if self.__distance is not None:
                query += "&distance={0}".format(self.__distance)

            if self.__units is not None:
                query += "&units={0}".format(self.__units)

            # TODO: !!!test!!!
            if len(self.__out_fields) > 0:
                fields = "*"
                if len(self.__out_fields) < len(self.fields):
                    fields = ",".join([f['name'] for f in self.__out_fields])
                query += "&outFields={0}".format(quote(fields))

            if self.__return_geometry is not None:
                query += "&returnGeometry={0}".format(self.__return_geometry)

            if self.__max_allowable_offset is not None:
                query += "&maxAllowableOffset={0}".format(self.__max_allowable_offset)

            if self.__geometry_precision is not None:
                query += "&geometryPrecision={0}".format(self.__geometry_precision)

            if self.__out_SR is not None:
                query += "&outSR={0}".format(self.__out_SR)

            if self.__return_ids_only is not None:
                query += "&returnIdsOnly={0}".format(self.__return_ids_only)

            if self.__return_count_only is not None:
                query += "&returnCountOnly={0}".format(self.__return_count_only)

            if self.__return_extent_only is not None:
                query += "&returnExtentOnly={0}".format(self.__return_extent_only)

            if len(self.__order_by_fields) > 0:
                query += "&orderByFields={0}".format(quote(",".join(self.__out_statistics)))

            # TODO: !!!test!!!
            if len(self.__out_statistics) > 0:
                query += "&outStatistics=[{0}]".format(quote(",".join([s.get_query_value for s in self.__out_statistics])))

            # TODO: !!!test!!!
            if len(self.__group_by_fields_statistics) > 0:
                query += "&groupByFieldsStatistics={0}".format(quote(",".join(self.__group_by_fields_statistics)))

            if self.__return_Z is not None:
                query += "&returnZ={0}".format(self.__return_Z)

            if self.__return_M is not None:
                query += "&returnM={0}".format(self.__return_M)

            if self.__gdb_version is not None:
                query += "&gdbVersion={0}".format(self.__gdb_version)

            if self.__return_distinct_values is not None:
                query += "&returnDistinctValues={0}".format(self.__return_distinct_values)

            if self.__return_true_curves is not None:
                query += "&returnTrueCurves={0}".format(self.__return_true_curves)

            if self.__result_offset is not None:
                query += "&resultOffset={0}".format(self.__result_offset)

            if self.__result_record_count is not None:
                query += "&resultRecordCount={0}".format(self.__result_record_count)

            # TODO: !!!test!!! need to understand format of datam transform parameters
            if self.__datum_transformation is not None:
                query += "&datumTransformation={0}".format(quote(self.__datum_transformation))

            if len(self.__range_values) > 0:
                query += "&rangeValues=[{0}]".format(quote(",".join(self.__range_values)))

            if len(self.__parameter_values) > 0:
                query += "&parameterValues={0}".format(quote(",".join(self.__parameter_values)))

            if self.__historic_moment is not None:
                query += "&historicMoment={0}".format(self.__historic_moment)

            self.value = query
            return self.value
        except Exception as e:
            exc_type, exc_obj, exc_tb = exc_info()
            f_name = split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(e, exc_type, f_name, exc_tb.tb_lineno)
            return str(e)

    def __repr__(self):
        self.get_query_string()
        return self.value

    def __str__(self):
        self.get_query_string()
        return self.value
