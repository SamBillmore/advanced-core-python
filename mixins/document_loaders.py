import csv
import io
import json

from utils import fake_requests as requests
from utils.utils import load_document


class DocumentLoader:
    def __init__(self, location):
        self.location = location

    def read(self):
        with open(self.location) as file:
            return file.read()

    def parse(self, item):
        return item  # This method exists to be extended by subclasses.

    def load(self):
        load_document(
            {
                'location': str(self.location),
                'contents': self.parse(self.read()),
            }
        )


class ParseCsvMixin:
    def parse(self, data):
        file_data = io.StringIO(data)
        reader = csv.DictReader(file_data)
        return list(reader)
    

class ParseJsonMixin:
    _data_to_return = None

    def parse(self, data):
        if self._data_to_return is None:
            raise AttributeError("_data_to_return attribute cannot be None")
        parsed_data = json.loads(data)
        return parsed_data[self._data_to_return]
    

class ReadFromUrlMixin:
    location = None

    def read(self):
        if self.location is None:
            raise AttributeError("location attribute cannot be None")
        return requests.get(self.location)


class LocalJsonLoader(ParseJsonMixin, DocumentLoader):
    _data_to_return = 'data'


class LocalCsvLoader(ParseCsvMixin, DocumentLoader):
    pass


class RemoteJsonLoader(ReadFromUrlMixin, ParseJsonMixin, DocumentLoader):
    _data_to_return = 'values'
    

class RemoteCsvLoader(ReadFromUrlMixin, ParseCsvMixin, DocumentLoader):
    pass


# ------------------------------------------------------------------------------
# DON'T EDIT BELOW HERE - it's just to check that your code is working
# ------------------------------------------------------------------------------

import pathlib
data_dir = pathlib.Path(__file__).parent / 'data'

print("\nExample Cases")
DocumentLoader(data_dir / 'demo_txt.txt').load()
LocalJsonLoader(data_dir / 'demo_json.json').load()
LocalCsvLoader(data_dir / 'demo_csv.csv').load()
RemoteJsonLoader("http://fake-json-source.com").load()
RemoteCsvLoader("http://fake-csv-source.com").load()
