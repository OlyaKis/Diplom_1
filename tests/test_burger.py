import pytest
from src.burger import Burger
from unittest.mock import MagicMock
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_mock():
    bun = MagicMock()
    bun.get_name.return_value = "Sesame Bun"
    bun.get_price.return_value = 2.0
    return bun


@pytest.fixture
def ingredient_mock():
    ing = MagicMock()
    ing.get_name.return_value = "Ketchup"
    ing.get_price.return_value = 0.5
    ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ing


def test_set_buns(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock


def test_add_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    assert ingredient_mock in burger.ingredients


def test_remove_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    burger.remove_ingredient(0)
    assert ingredient_mock not in burger.ingredients


def test_move_ingredient():
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


def test_get_price(bun_mock, ingredient_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    assert burger.get_price() == 2.0 * 2 + 0.5


def test_get_receipt(bun_mock, ingredient_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    receipt = burger.get_receipt()

    assert "sesame bun" in receipt.lower()
    assert "sauce ketchup" in receipt.lower()
    assert "price: 4.5" in receipt.lower()


def test_get_price_without_bun():
    burger = Burger()
    with pytest.raises(AttributeError) as exc_info:
        burger.get_price()
    assert "get_price" in str(exc_info.value)


def test_get_receipt_without_bun():
    burger = Burger()
    with pytest.raises(AttributeError) as exc_info:
        burger.get_receipt()
    assert "get_name" in str(exc_info.value)


def test_remove_ingredient_invalid_index(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    with pytest.raises(IndexError) as exc_info:
        burger.remove_ingredient(5)
    assert isinstance(exc_info.value, IndexError)
    assert "index out of range" in str(exc_info.value).lower()


def test_move_ingredient_invalid_index(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    with pytest.raises(IndexError) as exc_info:
        burger.move_ingredient(5, 0)
    assert isinstance(exc_info.value, IndexError)
    assert "index out of range" in str(exc_info.value).lower()


def test_get_receipt_multiple_ingredients(bun_mock):
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
    assert "sauce mayo" in receipt.lower()
    assert "filling bacon" in receipt.lower()
    assert "price:" in receipt.lower()


def test_get_price_without_ingredients(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.get_price() == 2.0 * 2  # только булки


def test_get_receipt_without_ingredients(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    receipt = burger.get_receipt()
    assert "price: 4.0" in receipt.lower()
    assert "==== sesame bun ====" in receipt.lower()


def test_get_price_without_bun():
    burger = Burger()
    with pytest.raises(AttributeError) as exc_info:
        burger.get_price()
    assert "get_price" in str(exc_info.value)


