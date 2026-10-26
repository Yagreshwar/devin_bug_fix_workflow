from decimal import Decimal


def apply_percentage_discount(amount, discount_percent):
    """Apply a percentage discount to an amount."""
    discount = Decimal(str(discount_percent)) / Decimal("100")
    return amount * (Decimal("1") - discount)
