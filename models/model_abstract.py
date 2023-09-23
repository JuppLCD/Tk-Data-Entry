from abc import ABC, abstractmethod

from utils.entities import User


class UserModelAbstract(ABC):

    # @abstractmethod
    # def getAll(self):
    #     pass

    # @abstractmethod
    # def getBy(self):
    #     pass

    @abstractmethod
    def store(self, data: User):
        pass

    # @abstractmethod
    # def update(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass
