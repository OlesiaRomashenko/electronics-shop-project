"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

import pytest


@pytest.fixture
def class_instance():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def child_class_instance():
    return Phone()


def test_init(class_instance):
    assert class_instance._Item__name == "Смартфон"
    assert class_instance.price == 10000
    assert class_instance.quantity == 20
    assert class_instance is class_instance.__class__.all[0]


def test_get_name(class_instance):
    assert class_instance.name == "Смартфон"


def test_set_name(class_instance):
    class_instance.name = 'СуперСмартфон'
    assert class_instance.name == "СуперСмарт"


def test_instantiate_from_csv(class_instance):
    class_instance.instantiate_from_csv('../src/items.csv')
    assert len(class_instance.all) == 5


def test_string_to_number(class_instance):
    assert class_instance.string_to_number('5') == 5
    assert class_instance.string_to_number('5.0') == 5
    assert class_instance.string_to_number('5.5') == 5


def test_calculate_total_price(class_instance):
    assert class_instance.calculate_total_price() == 200000


def test_apply_discount(class_instance):
    assert class_instance.apply_discount() == None


def test_str(class_instance):
    assert str(class_instance) == 'Смартфон'


def test_repr(class_instance):
    assert repr(class_instance) == "Item('Смартфон', 10000, 20)"

def test_add(class_instance):
    pass