import pytest

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


def test_str_product(first_product):
    assert (
        str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_add_product(first_product, second_product):
    assert first_product + second_product == 2580000


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_smartphone_add(first_smartphone, second_smartphone):
    assert first_smartphone + second_smartphone == 2580000.0
    with pytest.raises(TypeError):
        first_smartphone + 1


def test_lawngrass_init(first_grass):
    assert first_grass.name == "Газонная трава"
    assert first_grass.description == "Элитная трава для газона"
    assert first_grass.price == 500.0
    assert first_grass.quantity == 20
    assert first_grass.country == "Россия"
    assert first_grass.germination_period == "7 дней"
    assert first_grass.color == "Зеленый"


def test_lawngrass_add(first_grass, second_grass):
    assert first_grass + second_grass == 16750.0
    with pytest.raises(TypeError):
        first_grass + 1
