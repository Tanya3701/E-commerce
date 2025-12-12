import pytest


def test_first_product_iterator(first_product_iterator):
    iter(first_product_iterator)
    assert first_product_iterator.index == 0
    assert next(first_product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(first_product_iterator).name == "Iphone 15"
    assert next(first_product_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(first_product_iterator)
