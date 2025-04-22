import pytest
from src.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("Белая булочка", 2.5),
        ("Чёрная булочка", 3.0),
        ("Булочка с кунжутом", 3.5),
    ]
)
def test_bun_getters(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price


@pytest.mark.parametrize(
    "name, price",
    [
        ("Булка", 0.0),
        ("Булка", -1.0),
        ("", 1.0),
        ("a" * 1000, 999999.99),
    ]
)
def test_bun_extreme_values(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


def test_bun_type_flexibility():
    bun = Bun("Булочка", 2.5)
    assert isinstance(bun.get_name(), str)
    assert isinstance(bun.get_price(), (int, float))


def test_bun_price_type():
    bun = Bun("Булочка", 2.5)
    assert isinstance(bun.get_price(), float)  # или int, если цена целочисленная


def test_bun_name_type():
    bun = Bun("Булочка", 3.0)
    assert isinstance(bun.get_name(), str)


def test_bun_get_name():
    bun = Bun("Булочка с кунжутом", 2.5)
    assert bun.get_name() == "Булочка с кунжутом"


def test_bun_get_price():
    bun = Bun("Булочка", 3.0)
    assert bun.get_price() == 3.0


def test_bun_equality():
    bun1 = Bun("Чёрная булочка", 3.0)
    bun2 = Bun("Чёрная булочка", 3.0)
    assert bun1.get_name() == bun2.get_name()
    assert bun1.get_price() == bun2.get_price()


def test_bun_inequality():
    bun1 = Bun("Чёрная булочка", 3.0)
    bun2 = Bun("Белая булочка", 2.5)
    assert bun1.get_name() != bun2.get_name()
    assert bun1.get_price() != bun2.get_price()


def test_bun_str_name():
    bun = Bun("Булочка с кунжутом", 2.5)
    assert str(bun.get_name()) == "Булочка с кунжутом"


def test_bun_price_type():
    bun = Bun("Булочка", 3.75)
    assert isinstance(bun.get_price(), float)


def test_bun_zero_price():
    bun = Bun("Пустая булочка", 0.0)
    assert bun.get_price() == 0.0


def test_bun_negative_price():
    bun = Bun("Булочка-долг", -5.0)
    assert bun.get_price() == -5.0


def test_bun_empty_name():
    bun = Bun("", 1.0)
    assert bun.get_name() == ""


def test_bun_special_chars_name():
    bun = Bun("@Бул#очка$", 4.0)
    assert bun.get_name() == "@Бул#очка$"


def test_bun_large_price():
    bun = Bun("Золотая булочка", 1e6)
    assert bun.get_price() == 1e6


def test_bun_name_with_spaces():
    bun = Bun("   Булочка   ", 2.0)
    assert bun.get_name().strip() == "Булочка"


def test_bun_unicode_name():
    bun = Bun("Булочка 🌟", 2.2)
    assert "🌟" in bun.get_name()


def test_bun_name_numeric_string():
    bun = Bun("12345", 1.0)
    assert bun.get_name() == "12345"


def test_bun_price_rounding():
    bun = Bun("Булочка округления", 2.4999)
    assert round(bun.get_price(), 2) == 2.5


def test_bun_float_name_weird_case():
    bun = Bun(str(3.1415), 2.0)
    assert bun.get_name() == "3.1415"


def test_bun_multiple_instances_different_names():
    bun1 = Bun("Булка 1", 1.0)
    bun2 = Bun("Булка 2", 2.0)
    assert bun1.get_name() != bun2.get_name()


def test_bun_multiple_instances_same_price():
    bun1 = Bun("Булка 1", 5.0)
    bun2 = Bun("Булка 2", 5.0)
    assert bun1.get_price() == bun2.get_price()


def test_bun_name_very_long():
    long_name = "Булочка" * 100
    bun = Bun(long_name, 10.0)
    assert bun.get_name().startswith("Булочка")


def test_bun_name_is_none():
    bun = Bun(None, 3.0)
    assert bun.get_name() is None


def test_bun_price_is_none():
    bun = Bun("Булочка с пустотой", None)
    assert bun.get_price() is None


def test_bun_name_is_list():
    name = ["бул", "ка"]
    bun = Bun(name, 3.0)
    assert bun.get_name() == name


def test_bun_price_is_list():
    price = [1, 2, 3]
    bun = Bun("Булочка", price)
    assert bun.get_price() == price


def test_bun_name_is_dict():
    name = {"название": "Булка"}
    bun = Bun(name, 4.0)
    assert bun.get_name() == name


def test_bun_price_is_dict():
    price = {"price": 5.0}
    bun = Bun("Булка с прайсом в JSON", price)
    assert bun.get_price() == price


def test_bun_name_is_callable():
    bun = Bun(lambda: "Булочка", 2.0)
    assert callable(bun.get_name())


def test_bun_price_is_callable():
    bun = Bun("Булка", lambda: 2.0)
    assert callable(bun.get_price())


def test_bun_price_from_stringified_number():
    bun = Bun("Булочка", float("5.5"))
    assert bun.get_price() == 5.5


def test_bun_with_empty_string_name():
    bun = Bun("", 1.0)
    assert bun.get_name() == ""


def test_bun_with_zero_price():
    bun = Bun("Булка по акции", 0)
    assert bun.get_price() == 0


def test_bun_with_negative_price():
    bun = Bun("Контрафактная булочка", -5.0)
    assert bun.get_price() == -5.0


def test_bun_with_very_large_price():
    bun = Bun("Золотая булка", 1e10)
    assert bun.get_price() == 1e10


def test_bun_with_unicode_name():
    bun = Bun("Булочка с сюрпризом 🥐", 3.0)
    assert "🥐" in bun.get_name()


def test_bun_name_is_boolean():
    bun = Bun(True, 2.5)
    assert bun.get_name() is True


def test_bun_price_is_boolean():
    bun = Bun("Булочка-правда", False)
    assert bun.get_price() is False


def test_bun_name_is_number():
    bun = Bun(123456, 3.14)
    assert bun.get_name() == 123456


def test_bun_price_is_stringified_float():
    bun = Bun("Булочка", float("3.14159"))
    assert abs(bun.get_price() - 3.14159) < 1e-5

