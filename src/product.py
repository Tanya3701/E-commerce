from src.base_ptoduct import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс продукты"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        self.__price = price
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_dict):
        """Создает объект класса Product"""
        return cls(**new_dict)

    @property
    def price(self):
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Проверяет внедряемые цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            price_input = input(
                "Хотите изменить цену ниже текущей? 'y' - 'да'/ 'n' - нет:"
            )
            if price_input == "y":
                self.__price = new_price
            else:
                self.__price = self.__price
            return
        return


class Smartphone(Product):
    """класс Смартфоны"""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    """Класс Трава газонная"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
