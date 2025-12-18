from src.product import LawnGrass, Product, Smartphone


def test_print_mixin(capsys):
    Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    message = capsys.readouterr()
    assert message.out == 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)\n'
    Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    message = capsys.readouterr()
    assert message.out == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    message = capsys.readouterr()
    assert (
        message.out
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)\n"
    )
