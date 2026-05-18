from bot.client import get_client
from bot.logging_config import logger

client = get_client()

def place_market_order(symbol,side,quantity):
	
	try :
		logger.info(
			f"Placing MARKET order | Symbol={symbol} Side={side} Quantity={quantity}"
			)
		
		response = client.futures_create_order(
				symbol = symbol,
				side = side ,
				type = "MARKET",
				quantity = quantity
				)
		
		logger.info(f"Order Response: {response}")

		return response 
	
	except Exception as e :
		
		logger.error(f"MARKET Order Failed: {e}")

		raise Exception(f"MARKET order failed: {e}")


def place_limit_order(symbol,side,quantity,price):
	
	try :
		logger.info(
			f"Placing LIMIT order | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
			)

		response = client.futures_create_order(
				symbol=symbol,
				side=side,
				type="LIMIT",
				quantity=quantity,
				price=price,
				timeInForce="GTC"
				)
		
		logger.info(f"Order Response: {response}")

		return response
	
	except Exception as e :
		logger.error(f"LIMIT Order Failed: {e}")
		
		raise Exception(f"LIMIT order failed: {e}")
