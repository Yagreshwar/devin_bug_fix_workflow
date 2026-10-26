from decimal import Decimal

from orders.checkout import calculate_order_total


def test_order_total_without_discount_or_tax():
    items = [{"price": "100.00", "quantity": 1}]

    result = calculate_order_total(items)

    assert result["subtotal"] == Decimal("100.00")
    assert result["discount"] == Decimal("0.00")
    assert result["tax"] == Decimal("0.00")
    assert result["total"] == Decimal("100.00")


def test_order_total_with_discount_before_tax():
    items = [{"price": "100.00", "quantity": 1}]

    result = calculate_order_total(
        items,
        discount_percent=20,
        tax_rate=0,
    )

    assert result["subtotal"] == Decimal("100.00")
    assert result["discount"] == Decimal("20.00")
    assert result["total"] == Decimal("80.00")


def test_order_total_twenty_percent_discount_is_eighty_before_tax():
    items = [{"price": "100.00", "quantity": 1}]

    result = calculate_order_total(items, discount_percent=20)

    assert result["discount"] == Decimal("20.00")
    assert result["total"] == Decimal("80.00")


def test_order_total_multiple_items_with_discount():
    items = [
        {"price": "30.00", "quantity": 2},
        {"price": "40.00", "quantity": 1},
    ]

    result = calculate_order_total(items, discount_percent=20)

    assert result["subtotal"] == Decimal("100.00")
    assert result["discount"] == Decimal("20.00")
    assert result["total"] == Decimal("80.00")


def test_order_total_tax_applied_to_discounted_amount():
    items = [{"price": "100.00", "quantity": 1}]

    result = calculate_order_total(
        items,
        discount_percent=20,
        tax_rate="0.10",
    )

    assert result["subtotal"] == Decimal("100.00")
    assert result["discount"] == Decimal("20.00")
    assert result["tax"] == Decimal("8.00")
    assert result["total"] == Decimal("88.00")
