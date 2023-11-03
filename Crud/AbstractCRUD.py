from abc import ABC, abstractmethod
from typing import overload


class CRUD(ABC):

    def __init__(self, conection):
        self.__conection = conection
        self.__cursor = self.__conection.cursor()


    @abstractmethod
    def Create(self, object: object):
        raise NotImplementedError()

    @abstractmethod
    def Read(self):
        raise NotImplementedError()

    @overload
    @abstractmethod
    def Read(self, id: int) -> object:
        raise NotImplementedError()

    @abstractmethod
    def Delete(self, id):
        raise NotImplementedError()

    @abstractmethod
    def Update(self, id: int , object: object):
        NotImplementedError()




