from src.product import Product
from src.user_exceptions import UserException


class Category:
    """Класс категории"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0

    def __str__(self):
        inventory_level = []
        for product in self.__products:
            inventory_level.append(product.quantity)
        return f"{self.name}, количество продуктов: {sum(inventory_level)} шт."

    def add_product(self, product):
        """Метод для добавления товаров в категорию"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise UserException("Количество товара не может быть равное нулю")
            except UserException as e:
                print(e)
            else:
                self.__products.append(product)
                self.product_count += 1
                print("Товар добавлен")
            finally:
                print("Информация о товаре обработана")
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер, который выводит список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @products.setter
    def products(self, new_product: Product):
        if isinstance(new_product, Product):
            self.add_product(new_product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def product_list(self):
        return self.__products

    def total_quantity(self):
        inventory_level = []
        for product in self.__products:
            inventory_level.append(product.quantity)
        return sum(inventory_level)

    def middle_price(self):
        """Выводит среднюю цену товара"""
        try:
            return round(
                sum(product.price for product in self.__products)
                / len(self.__products),
                1,
            )
        except ZeroDivisionError:
            return 0
