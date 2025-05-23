import pytest
from src.burger import Burger
from unittest.mock import MagicMock
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients

    def test_move_ingredient(self):
        ing1 = MagicMock()
        ing1.get_name.return_value = "Cheese"
        ing1.get_price.return_value = 1.0
        ing1.get_type.return_value = INGREDIENT_TYPE_FILLING
        ing2 = MagicMock()
        ing2.get_name.return_value = "Lettuce"
        ing2.get_price.return_value = 0.5
        ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger = Burger()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ing2, ing1]

    def test_get_price(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 2.0 * 2 + 0.5

    def test_get_receipt(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= sauce Ketchup =\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 4.5"
        )
        assert receipt == expected_receipt

    def test_get_price_without_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError) as exc_info:
            burger.get_price()
        assert "get_price" in str(exc_info.value)

    def test_get_receipt_without_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError) as exc_info:
            burger.get_receipt()
        assert "get_name" in str(exc_info.value)

    def test_remove_ingredient_invalid_index_raises(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        with pytest.raises(IndexError) as exc_info:
            burger.remove_ingredient(5)
        assert exc_info.value is not None

    def test_remove_ingredient_invalid_index_message(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        with pytest.raises(IndexError) as exc_info:
            burger.remove_ingredient(5)
        assert "index out of range" in str(exc_info.value).lower()

    def test_move_ingredient_invalid_index_raises(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        with pytest.raises(IndexError) as exc_info:
            burger.move_ingredient(5, 0)
        assert exc_info.value is not None

    def test_move_ingredient_invalid_index_message(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        with pytest.raises(IndexError) as exc_info:
            burger.move_ingredient(5, 0)
        assert "index out of range" in str(exc_info.value).lower()

    def test_get_receipt_contains_mayo(self, bun_mock):
        ing1 = MagicMock()
        ing1.get_name.return_value = "Mayo"
        ing1.get_price.return_value = 0.2
        ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ing1)
        receipt = burger.get_receipt()
        assert "= sauce Mayo =" in receipt

    def test_get_receipt_contains_bacon(self, bun_mock):
        ing2 = MagicMock()
        ing2.get_name.return_value = "Bacon"
        ing2.get_price.return_value = 1.5
        ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ing2)
        receipt = burger.get_receipt()
        assert "= filling Bacon =" in receipt

    def test_get_receipt_price_multiple_ingredients(self, bun_mock):
        ing1 = MagicMock()
        ing1.get_name.return_value = "Mayo"
        ing1.get_price.return_value = 0.2
        ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ing2 = MagicMock()
        ing2.get_name.return_value = "Bacon"
        ing2.get_price.return_value = 1.5
        ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        receipt = burger.get_receipt()
        assert "Price: 5.7" in receipt

    def test_get_price_without_ingredients(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.get_price() == 2.0 * 2

    def test_get_receipt_without_ingredients(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 4.0"
        )
        assert receipt == expected_receipt
