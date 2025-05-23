import pytest
from src.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name",
        [
            "Белая булочка",
            "Чёрная булочка",
            "Булочка с кунжутом",
            "",
            "Булочка 🌟",
            "12345",
        ]
    )
    def test_get_name(self, name):
        bun = Bun(name, 2.5)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [
            2.5,
            0.0,
            -1.0,
            999999.99,
            1e6,
        ]
    )
    def test_get_price(self, price):
        bun = Bun("Булка", price)
        assert bun.get_price() == price

    def test_get_name_type(self):
        bun = Bun("Булочка", 3.0)
        assert isinstance(bun.get_name(), str)

    def test_get_price_type(self):
        bun = Bun("Булочка", 2.5)
        assert isinstance(bun.get_price(), float) or isinstance(bun.get_price(), int)

    def test_get_name_empty(self):
        bun = Bun("", 1.0)
        assert bun.get_name() == ""

    def test_get_price_zero(self):
        bun = Bun("Пустая булочка", 0.0)
        assert bun.get_price() == 0.0

    def test_get_price_negative(self):
        bun = Bun("Булочка-долг", -5.0)
        assert bun.get_price() == -5.0

    def test_get_name_unicode(self):
        bun = Bun("Булочка с сюрпризом 🥐", 3.0)
        assert "🥐" in bun.get_name()

    def test_get_price_large(self):
        bun = Bun("Золотая булка", 1e10)
        assert bun.get_price() == 1e10
