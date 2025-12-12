class Product:
    """Класс продукты"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

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
