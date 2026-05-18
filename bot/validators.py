VALID_SIDES = ["BUY","SELL"]
VALID_ORDER_TYPES = ["MARKET","LIMIT"]

def validate_side(side):
	if side.upper() not in VALID_SIDES:
		raise ValueError(
			f"Invalid side: {side} . Must be BUY or SELL."
			)
	
def validate_order_type(order_type):
	if order_type.upper() not in VALID_ORDER_TYPES :
		raise ValueError(
			f"Invalid order type: {order_type}. Must be MARKET or LIMIT."
		)

def validate_quantity(quantity):
	
	if quantity <= 0 :
		raise ValueError(
			"Quantity must be greater than 0."
		)

def validate_price(price) :
	
	if price <= 0:
		raise ValueError(
			"Price must be greater than 0."
		)
