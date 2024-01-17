"""Здесь написаны тесты с использованием pytest для модуля Phone"""
from src.phone import Phone

import pytest


@pytest.fixture
def class_instance():
    return Phone("Смартфон", 10000, 20, 2)


def test_get_number_of_sim(class_instance):
    assert class_instance.number_of_sim == 2


def test_set_number_of_sim(class_instance):
    class_instance.number_of_sim = 0
    with pytest.raises(ValueError):
        number_of_sim(class_instance, v)
