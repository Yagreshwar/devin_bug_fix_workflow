from decimal import Decimal

import pytest

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


@pytest.mark.parametrize(
    "amount, discount_percent, expected",
    [
        (Decimal("100.00"), 10, Decimal("90.00")),
        (Decimal("100.00"), 25, Decimal("75.00")),
        (Decimal("100.00"), 50, Decimal("50.00")),
        (Decimal("59.99"), 20, Decimal("47.992")),
        (Decimal("100.00"), "12.5", Decimal("87.50")),
    ],
)
def test_percentage_discount_reduces_amount_by_full_percentage(
    amount, discount_percent, expected
):
    assert apply_percentage_discount(amount, discount_percent) == expected
