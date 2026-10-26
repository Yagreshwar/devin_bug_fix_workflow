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


def test_discount_reduces_by_full_percentage_regression():
    # Regression: discount was previously divided by 5 (20% -> 4%).
    assert apply_percentage_discount(Decimal("100.00"), 20) != Decimal("96.00")
    assert apply_percentage_discount(Decimal("100.00"), 50) == Decimal("50.00")
    assert apply_percentage_discount(Decimal("100.00"), 10) == Decimal("90.00")


def test_fractional_percentage_discount():
    assert apply_percentage_discount(
        Decimal("200.00"), "12.5"
    ) == Decimal("175.00")
