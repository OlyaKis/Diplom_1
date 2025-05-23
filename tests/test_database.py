from src.database import Database
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_buns_first_name(self):
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_buns_second_price(self):
        db = Database()
        buns = db.available_buns()
        assert buns[1].get_price() == 200

    def test_buns_all_positive_price(self):
        db = Database()
        buns = db.available_buns()
        assert all(bun.get_price() > 0 for bun in buns)

    def test_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_ingredients_sauces_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_ingredients_fillings_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_ingredients_contains_cutlet(self):
        db = Database()
        ingredients = db.available_ingredients()
        names = [i.get_name() for i in ingredients]
        assert "cutlet" in names

    def test_ingredients_contains_hot_sauce(self):
        db = Database()
        ingredients = db.available_ingredients()
        names = [i.get_name() for i in ingredients]
        assert "hot sauce" in names
