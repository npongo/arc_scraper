from abc import ABC, abstractmethod
from helpers import sanitize_and_quote_name, exception_logging, sanitize_name, escape_insert
from datetime import datetime


class DBClient(ABC):

    def __init__(self, db_conn):
        self._db_conn = db_conn
        self._sql_generator_templates = {}
        self._sql_generator_options = {}

    @property
    def name(self):
        return self._sql_generator_options['name']

    @property
    def sql_generator_templates(self):
        return self._sql_generator_templates

    @sql_generator_templates.setter
    def sql_generator_templates(self, value):
        for k, v in value:
            self._sql_generator_templates[k] = v

    @property
    def sql_generator_options(self):
        return self._sql_generator_options

    @sql_generator_options.setter
    def sql_generator_options(self, value):
        for k, v in value:
            self._sql_generator_options[k] = v

    @property
    def db_conn(self):
        return self._db_conn

    @db_conn.setter
    def db_conn(self, value):
        self._db_conn = value

    def quote_name(self, name):
        quote_start = self.quote_characters[0]
        quote_end = (self.quote_characters + self.quote_characters)[1]
        if self.sql_generator_options['max_identifier_length'] < 0:
            name = name[self.sql_generator_options['max_identifier_length']:]
        else:
            name = name[:self.sql_generator_options['max_identifier_length']]

        if not name.startswith(quote_start):
            name = quote_start + name
        if not name.endswith(quote_end):
            name += quote_end
        return name

    def sanitize_and_quote_name(self, name):
        return sanitize_and_quote_name(name, self.quote_characters,
                                       max_length=self.sql_generator_options['max_identifier_length'],
                                       underscore_leading_number=True,
                                       allow_double_symbols = self.sql_generator_options['allow_double_symbols'],
                                       force_lower_case=self.sql_generator_options['use_lower_case_identifier'],
                                       replacement_dict=self.sql_generator_options['sanitize_replacements'])

    def sanitize_name(self, name):
        return sanitize_name(name, max_length=self.sql_generator_options['max_identifier_length'],
                             underscore_leading_number=True,
                             allow_double_symbols = self.sql_generator_options['allow_double_symbols'],
                             force_lower_case=self.sql_generator_options['use_lower_case_identifier'],
                             replacement_dict=self.sql_generator_options['sanitize_replacements'])

    @property
    def statement_terminator(self):
        return self._sql_generator_options['statement_terminator']

    @property
    def quote_characters(self):
        return self.sql_generator_options.get("quote_characters", "")

    def insert_safe(self, string):
        for k, v in self.sql_generator_options['insert_safe_characters'].items():
            string = string.replace(k, v)
        return string

    def string_date(self, date_value):
        if not isinstance(date_value, datetime):
            raise Exception("date_value must be a datetime object")
        return date_value.strftime(self.sql_generator_options['date_string_format'])

    @abstractmethod
    def exec_non_query(self, sql_statements, raise_on_fail=False):
        """

        :param sql_statements: a list of sql statements to execute that doe not return a result, primaryily meant
         for DDL slq
        :param raise_on_fail: stops execture of additional sql statements if true and raise the exception, otherwise
        exceptions are logged
        :return: None
        """
        pass

    @abstractmethod
    def exec_scalar_query(self, sql_statement):
        """
        execute an sql query against the sql server database that returns a scalar value
        :param sql_statement: an sql statement that returns a scalar value
        :return: scaler
        """
        pass
    
    def exec_result_set_query(self, sql_statement):
        """
        execute an sql query against the sql server database that returns a scalar value
        :param sql_statement: an sql statement that returns a scalar value
        :return: scaler
        """
        pass 

    @staticmethod
    def chunker(seq, size):
        """
        groups a list into a list of chunks
        :param seq: input sequence or list
        :param size: sizs of the chunk to group the seq into
        :return: a list of lists, the inner list has the length of size
        """
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    @abstractmethod
    def run_bulk_insert(self, insert_template, data, formatter, batch=1000):
        """

        :param insert_template: template used to insert data
        :param data: iterable of rows of data
        :param formatter: function used to format row of data
        :param batch:
        :return:
        """
        pass

    def log_error(self, error_att):
        """
        logs and exception into the database.
        :param error_att: dictionary of error column values
        :return: None
        """
        error_template = self.sql_generator_templates['insert_error'].format(**error_att)
        self.exec_non_query(error_template)

    def escape_insert(self, row):
        """

        :param row: a row of data as either a list of values or a dictionary of columns(keys) and values
        :return: row escaped and quoted
        """
        date_string_format = self.sql_generator_options['date_string_format']
        text_qoute = self.sql_generator_options['text_qoute']
        escape_characters = self.sql_generator_options['escape_characters']
        new_row = escape_insert(row, text_qoute=text_qoute,
                                escape_characters=escape_characters,
                                date_formater=date_string_format)
        return new_row