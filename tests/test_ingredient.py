import pytest
from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Кетчуп", 0.5),
            (INGREDIENT_TYPE_FILLING, "Котлета", 1.5),
            (INGREDIENT_TYPE_FILLING, "Сыр", 0.8),
            (INGREDIENT_TYPE_SAUCE, "Майонез", 0.4),
        ]
    )
    def test_ingredient_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
