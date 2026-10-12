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
