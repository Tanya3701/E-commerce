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
        self.price = price
