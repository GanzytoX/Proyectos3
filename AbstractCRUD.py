from abc import ABC, abstractmethod

class CRUD(ABC):
    @abstractmethod
    def editar(self, id):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass

    @abstractmethod
    def get(self, id=None):
        pass

