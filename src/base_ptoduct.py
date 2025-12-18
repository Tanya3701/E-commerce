from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для классов продукты"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
