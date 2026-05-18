import argparse
import logging_config

from orders import place_market_order, place_limit_order
from validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = float(args.quantity)
    price = args.price

    # validations
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    validate_price(order_type, price)

    print("\n===== ORDER SUMMARY =====")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")

    if price:
        print(f"Price: {price}")

    print("=========================\n")

    # place order
    if order_type == "MARKET":
        response = place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        response = place_limit_order(symbol, side, quantity, price)

    # print response
    if response:
        print("===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print("==========================")

        print("\nOrder placed successfully!")

except Exception as e:
    print(f"Validation/Error: {e}")