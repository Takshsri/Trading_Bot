from client import client
import logging_config
import logging
logger = logging.getLogger(__name__)

def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Market order successful: {order}")

        return order

    except Exception as e:
        logger.error(f"Market order failed: {e}")
        print("Error:", e)


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} at {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Limit order successful: {order}")

        return order

    except Exception as e:
        logger.error(f"Limit order failed: {e}")
        print("Error:", e)