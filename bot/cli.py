import argparse

from bot.orders import (
		place_market_order,
		place_limit_order
		)

from bot.validators import(
		validate_side,
		validate_order_type,
		validate_quantity,
		validate_price
		)

parser = argparse.ArgumentParser(
	description="Binance Futures Testnet trading Bot"
	)

parser.add_argument("--symbol", required=True, help="Trading symbol")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try :
	validate_side(args.side)
	validate_order_type(args.type)
	validate_quantity(args.quantity)
	
	if args.type.upper() == "LIMIT" :
		if args.price is None:
			raise ValueError(
				"Price is required for LIMIT orders."
			)
		
		validate_price(args.price)
		
		response = place_limit_order(
			symbol=args.symbol,
			side=args.side.upper(),
			quantity=args.quantity,
			price=args.price
			)
	else :
	
		response = place_market_order(
			symbol=args.symbol,
			side=args.side,
			quantity=args.quantity
			)
	
	print("\n===== ORDER RESPONSE =====")
	print(f"Symbol: {response['symbol']}")
	print(f"Side: {response['side']}")
	print(f"Type: {response['type']}")
	print(f"Status: {response['status']}")
	print(f"Order ID: {response['orderId']}")
	print(f"Quantity: {response['origQty']}")
	print(f"Executed Quantity: {response['executedQty']}")
	print(f"Average Price: {response['avgPrice']}")

except Exception as e :
	print("\n===== ERROR =====")
	print(e)
