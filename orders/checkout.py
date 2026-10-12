from decimal import Decimal

from orders.discounts import apply_percentage_discount
from orders.pricing import calculate_subtotal, calculate_tax


def calculate_order_total(items, discount_percent=0, tax_rate=0):
    """Calculate subtotal, discount, tax, and final total."""
    subtotal = calculate_subtotal(items)
    discounted_total = apply_percentage_discount(
        subtotal, discount_percent
    )
    discount_amount = subtotal - discounted_total
    tax = calculate_tax(discounted_total, tax_rate)
    total = discounted_total + tax

    return {
        "subtotal": subtotal,
        "discount": discount_amount,
        "tax": tax,
        "total": total,
    }
