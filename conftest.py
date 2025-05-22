import pytest
from unittest.mock import MagicMock
from src.ingredient_types import INGREDIENT_TYPE_SAUCE


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
