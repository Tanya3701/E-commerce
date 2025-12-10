def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert first_category.category_count == 2
    assert len(first_category.product_list) == 3
    assert len(second_category.product_list) == 1


def test_products_property(first_category):
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra 180000.0 руб. Остаток: 5 шт."
        "\nIphone 15 210000.0 руб. Остаток: 8 шт."
        "\nXiaomi Redmi Note 11 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_products_setter(first_category, first_product):
    assert len(first_category.product_list) == 3
    first_category.products = first_product
    assert len(first_category.product_list) == 4
