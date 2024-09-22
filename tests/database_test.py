from praktikum.database import Database


class TestDatabase:
    """
    Тесты для класса Database
    """

    def test_database_available_buns(self):
        """
        Позитивный тест метода available_buns класса Database
        """
        database = Database()

        assert database.available_buns() == database.buns and len(database.available_buns()) == 3

    def test_database_available_ingredients(self):
        """
        Позитивный тест метода available_ingredients класса Database
        """
        database = Database()

        assert database.available_ingredients() == database.ingredients and len(database.available_ingredients()) == 6
