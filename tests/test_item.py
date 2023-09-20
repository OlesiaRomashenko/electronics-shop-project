"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

import pytest


@pytest.fixture
def class_instance():
    return Item("Смартфон", 10000, 20)


def test_init(class_instance):
    assert class_instance.name == "Смартфон"
    assert class_instance.price == 10000
    assert class_instance.quantity == 20
    assert class_instance is class_instance.__class__.all[0]


def test_calculate_total_price(class_instance):
    assert class_instance.calculate_total_price() == 200000


def test_apply_discount(class_instance):
    assert class_instance.apply_discount() == None
