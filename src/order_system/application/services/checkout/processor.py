from order_system.domain.pricing.calculator import calculate_total
from order_system.utils.currency import format_currency

def process_checkout(items):
    total = calculate_total(items)
    return format_currency(total)
