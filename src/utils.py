import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Преобразует json-файл в словарь"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def create_json(data: dict) -> list:
    """Реализует подгрузку данных по категориям и товарам из файла JSON"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
