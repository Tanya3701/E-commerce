from abc import ABC, abstractmethod


class BaseCategory(ABC):

    @abstractmethod
    def total_quantity(self):
        pass
