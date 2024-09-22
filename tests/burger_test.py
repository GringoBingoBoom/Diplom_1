import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """
    Тесты для класса Burger
    """

    dataset_set_buns = [
        ['bun#1', 100],
        ['bun#2', 110]
    ]

    dataset_add_ingredient = [
        [INGREDIENT_TYPE_SAUCE, "sause#1", 100],
        [INGREDIENT_TYPE_FILLING, "filling#1", 200],
    ]

    dataset_remove_ingredient = [
        [
            (INGREDIENT_TYPE_SAUCE, "sause#1", 100),
            (INGREDIENT_TYPE_SAUCE, "sause#2", 110)
        ]
    ]

    dataset_get_price = [
        [['bun#1', 100], [INGREDIENT_TYPE_SAUCE, "sause#1", 100], [INGREDIENT_TYPE_FILLING, "filling#1", 200], 500],
        [['bun#2', 101], [INGREDIENT_TYPE_SAUCE, "sause#2", 101], [INGREDIENT_TYPE_FILLING, "filling#2", 202], 505]
    ]

    get_receipt_expected_result = (f'(==== bun#1 ====)\n= sauce sause#1 =\n= filling '
                                   f'filling#1 =\n(==== bun#1 ====)\n\nPrice: 500')

    dataset_get_receipt = [
        [['bun#1', 100], [INGREDIENT_TYPE_SAUCE, "sause#1", 100], [INGREDIENT_TYPE_FILLING, "filling#1", 200],
         get_receipt_expected_result]
    ]

    @pytest.mark.parametrize('name, price', dataset_set_buns)
    def test_burger_set_buns(self, name, price):
        """
        Позитивный тест метода set_buns класса Burger с 2мя наборами данных
        """
        burger = Burger()

        mock_bun = Mock()  # создали мок-объект
        mock_bun.get_name.return_value = name  # указали возвращаемые значения для методов мока
        mock_bun.get_price.return_value = price  # указали возвращаемые значения для методов мока

        # передали мок-объект в метод set_buns
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, f'Объект burger.bun не равен mock_bun'

    @pytest.mark.parametrize('ingredients', dataset_add_ingredient)
    def test_burger_add_ingredient(self, ingredients):
        """
        Позитивный тест метода add_ingredient класса Burger с 2мя наборами данных
        """
        burger = Burger()

        mock_ingredient = Mock()  # создали мок-объект для mock_ingredient
        mock_ingredient.get_type.return_value = ingredients[0]  # указали возвращаемые значения для методов мока type
        mock_ingredient.get_name.return_value = ingredients[1]  # указали возвращаемые значения для методов мока name
        mock_ingredient.get_price.return_value = ingredients[2]  # указали возвращаемые значения для методов мока price

        # передали мок-объект в метод add_ingredient
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient], f'Объект burger.ingredients не равен [ingredient]'

    @pytest.mark.parametrize('ingredients', dataset_remove_ingredient)
    def test_burger_remove_ingredient_two_add_one_delete(self, ingredients):
        """
        Позитивный тест метода remove_ingredient класса Burger один набор данных
        """
        burger = Burger()
        ingredient1 = Ingredient(*ingredients[0])
        ingredient2 = Ingredient(*ingredients[1])
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient1], f'Объект burger.ingredients не равен [ingredient1]'

    @pytest.mark.parametrize('ingredients', dataset_remove_ingredient)
    def test_burger_move_ingredient_two_add_one_move(self, ingredients):
        """
        Позитивный тест метода move_ingredient класса Burger
        """
        burger = Burger()
        ingredient1 = Ingredient(*ingredients[0])
        ingredient2 = Ingredient(*ingredients[1])
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient2,
                                      ingredient1], f'Объект burger.ingredients не равен [ingredient2, ingredient1]'

    @pytest.mark.parametrize('bun, sauce, filling, expected_price', dataset_get_price)
    def test_burger_get_price(self, bun, sauce, filling, expected_price):
        """
        Позитивный тест метода get_price класса Burger с 2-мя наборами данных
        """
        burger = Burger()
        burger.set_buns(Bun(*bun))
        burger.add_ingredient(Ingredient(*sauce))
        burger.add_ingredient(Ingredient(*filling))

        assert burger.get_price() == expected_price, f'Значение burger.get_price() не равно expected_price'

    @pytest.mark.parametrize('bun, sauce, filling, get_receipt_expected_result', dataset_get_receipt)
    def test_burger_get_receipt(self, bun, sauce, filling, get_receipt_expected_result):
        """
        Позитивный тест метода get_receipt класса Burger
        """
        burger = Burger()
        burger.set_buns(Bun(*bun))
        burger.add_ingredient(Ingredient(*sauce))
        burger.add_ingredient(Ingredient(*filling))

        assert burger.get_receipt() == get_receipt_expected_result, (f'Значение burger.get_receipt() '
                                                                     f'не равно get_receipt_expected_result')
