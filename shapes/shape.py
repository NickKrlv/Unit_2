from abc import ABC, abstractmethod


class Shape(ABC):
    """ Base class for all shapes """
    @abstractmethod
    def area(self):
        pass
