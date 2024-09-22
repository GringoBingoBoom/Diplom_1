import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """
    Тесты для класса Ingredient
    """

    dataset_ingredient_get = [
        [INGREDIENT_TYPE_SAUCE, "sause#1", 100],
        [INGREDIENT_TYPE_FILLING, "filling#1", 200],
    ]

    @pytest.mark.parametrize('ingredient', dataset_ingredient_get)
    def test_get_price_set_and_check_price(self, ingredient):
        """
        Позитивный тест метода get_price класса Ingredient с 2-мя наборами данных
        """
        expected_price = ingredient[2]

        assert Ingredient(*ingredient).get_price() == expected_price, f'Значение get_price() не равно {expected_price}'

    @pytest.mark.parametrize('ingredient', dataset_ingredient_get)
    def test_get_name_set_and_check_name(self, ingredient):
        """
        Позитивный тест метода get_name класса Ingredient с 2-мя наборами данных
        """
        expected_name = ingredient[1]

        assert Ingredient(*ingredient).get_name() == expected_name, f'Значение get_name() не равно {expected_name}'

    @pytest.mark.parametrize('ingredient', dataset_ingredient_get)
    def test_get_type_set_and_check_price(self, ingredient):
        """
        Позитивный тест метода get_type класса Ingredient с 2-мя наборами данных
        """
        expected_type = ingredient[0]

        assert Ingredient(*ingredient).get_type() == expected_type, f'Значение get_type() не равно {expected_type}'
