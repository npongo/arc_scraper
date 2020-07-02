from abc import ABC, abstractmethod
from urllib.parse import urlparse
from sys import exc_info
from os.path import split
import requests
from helpers import exception_logging

# TODO add out_srid
class ArcBase(ABC):

    def __init__(self, uri, db_client):
        self._uri = uri  # if uri.endswith("/") else f"{uri}/"
        self._db_client = db_client
        self._loaded = False
        self._timeout = 50000
        self._raw_json = dict()
        self._errors = list()

    @property
    def loaded(self):
        return self._loaded

    @loaded.setter
    def loaded(self, value):
        self._loaded = value

    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    @property
    def db_client(self):
        return self._db_client

    @db_client.setter
    def db_client(self, value):
        self._db_client = value

    @property
    def raw_json(self):
        return self._raw_json

    @raw_json.setter
    def raw_json(self, value):
        self._raw_json = value

    @property
    def errors(self):
        return self._errors

    @property
    def sql(self):
        return self.generate_sql()

    def add_error(self, e):
        if isinstance(e, Exception):
            self._errors.append(e)
            exception_logging(e)

    @abstractmethod
    def generate_sql(self):
        pass

    @abstractmethod
    def generate_sql_extra(self):
        pass

    @abstractmethod
    def generate_sql_preamble(self):
        pass

    def run_sql(self):
        """

        :return:
        """
        try:
            db_name = str(urlparse(self._uri)['netloc']).replace("www.", "").replace('.', '_')
            if 'database' not in self._db_client.db_conn:
                self._db_client.db_conn['database'] = db_name
            sql_statements = self.generate_sql() + self.generate_sql_extra()
            self._db_client.exec_non_query(sql_statements)
        except Exception as e:
            self.add_error(e)

    @abstractmethod
    def load_meta_data(self):
        pass

    def load_json(self):
        """

        :return:
        """
        try:
            url = f"{self._uri}?f=json"
            result = requests.get(url)
            if result.ok:
                if 'error' in result.json():
                    self.add_error(Exception(f"load error {result.text}"))
                else:
                    self._raw_json = result.json()
            else:
                self.add_error(Exception(f"failed to load {self.uri}, status_code {result.status_code}, "
                                         f"content: {result.text}"))
        except Exception as e:
            self.add_error(e)