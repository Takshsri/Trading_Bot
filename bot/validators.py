VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_side(side):
    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity):
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(order_type, price):
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")