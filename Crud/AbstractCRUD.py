from abc import ABC, abstractmethod

class CRUD(ABC):

    def __init__(self, conection):
        self.__conection = conection
        self.__cursor = self.__conection.cursor()


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




