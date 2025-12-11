from src.product import Product


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

    def add_product(self, product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        """Геттер, который выводит список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return product_str

    @products.setter
    def products(self, new_product: Product):
        self.add_product(new_product)
        self.product_count += 1

    @property
    def product_list(self):
        return self.__products
