from src.product import Product


def test_product_init(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_add_product():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 250000.0
    product.quantity = 8


def test_product_setter(capsys, first_product):
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"
    first_product.price = -20000.0
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"
    first_product.quantity = 250000.0
