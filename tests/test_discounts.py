from decimal import Decimal

from orders.discounts import apply_percentage_discount


def test_twenty_percent_discount():
    assert apply_percentage_discount(
        Decimal("100.00"), 20
    ) == Decimal("80.0000")


def test_zero_percent_discount():
    assert apply_percentage_discount(
        Decimal("100.00"), 0
    ) == Decimal("100.00")


def test_one_hundred_percent_discount():
    assert apply_percentage_discount(
        Decimal("100.00"), 100
    ) == Decimal("0.00")
