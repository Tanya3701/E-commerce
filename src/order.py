from base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):

    product: Product
    count: int
    total_amount: float

    def __init__(self, product, count):
        self.product = product
        self.count = count
        self.total_amount = self.product.price * count
        self.product.quantity -= count

    def __str__(self):
        return f"Заказ: {self.product.name} - {self.count} шт. на сумму {self.total_amount}"

    def total_quantity(self):
        return self.count
