import pytest
from praktikum.bun import Bun


class TestBun:
    """
    Тесты для класса Bun
    """
    dataset_bun = [
        ['булка#1', 100],
        ['булка#2', 110]
    ]

    @pytest.mark.parametrize('name, price', dataset_bun)
    def test_bun_get_name_check_value_name_get_as_set(self, name, price):
        """
        Позитивный тест метода get_name класса Bun с 2мя наборами данных
        """
        bun = Bun(name, price)

        assert bun.get_name() == name, f'Значение bun.get_name() не равно {name}'

    @pytest.mark.parametrize('name, price', dataset_bun)
    def test_bun_get_price_check_value_price_get_as_set(self, name, price):
        """
        Позитивный тест метода get_price класса Bun с 2мя наборами данных
        """
        bun = Bun(name, price)

        assert bun.get_price() == price, f'Значение bun.get_price() не равно {price}'
