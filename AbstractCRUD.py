from abc import ABC, abstractmethod

class CRUD(ABC):
    @abstractmethod
    def Update(self, id):
        pass

    @abstractmethod
    def Delete(self, id):
        pass

    @abstractmethod
    def get(self, id=None):
        pass



