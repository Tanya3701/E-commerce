def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.products == [
        ("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        ("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]
    assert first_category.category_count == 2
    assert len(first_category.products) == 3
    assert len(second_category.products) == 1
