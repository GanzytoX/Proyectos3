from abc import ABC, abstractmethod

class CRUD(ABC):

    @abstractmethod
    def Create(self, object: object):
        raise NotImplementedError()

    @abstractmethod
    def Read(self, id=None, condition=None):
        raise NotImplementedError()

    @abstractmethod
    def Delete(self, id):
        raise NotImplementedError()

    @abstractmethod
    def Update(self, id: int , object: object):
        NotImplementedError()




