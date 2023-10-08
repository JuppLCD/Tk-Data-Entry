from abc import ABC, abstractmethod


class ModelAbstract(ABC):

    @abstractmethod
    def getAll(self) -> list:
        pass

    # @abstractmethod
    # def getBy(self):
    #     pass

    @abstractmethod
    def store(self, data):
        pass

    # @abstractmethod
    # def update(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass
