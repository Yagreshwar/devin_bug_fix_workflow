
from decimal import Decimal


def calculate_subtotal(items):
    """Calculate the subtotal from item prices and quantities."""
    return sum(
        (Decimal(str(item["price"])) * item["quantity"] for item in items),
        Decimal("0.00"),
    )


def calculate_tax(amount, tax_rate):
    """Calculate tax on an amount."""
    return (amount * Decimal(str(tax_rate))).quantize(Decimal("0.01"))
