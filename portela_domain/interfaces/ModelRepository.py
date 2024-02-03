from abc import ABC
from tarfile import data_filter


class ModelRepository(ABC):
    
    def create(self, model):
        pass

    def read(self, id):
        pass

    def update(self, model):
        pass

    def delete(self, id):
        pass

    def list(self):
        pass

    def query(self, query: data_filter):
        pass