from src.database import Database
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_available_buns():
    db = Database()
    buns = db.available_buns()

    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_price() == 200
    assert all(bun.get_price() > 0 for bun in buns)


def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()

    assert len(ingredients) == 6

    sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
    fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

    assert len(sauces) == 3
    assert len(fillings) == 3

    names = [i.get_name() for i in ingredients]
    assert "cutlet" in names
    assert "hot sauce" in names
