
def Add(value1,value2):
	Addition = value1 + value2
	return Addition

def Sub(value1, value2):
	Substraction = value1 - value2
	return Substraction

def Mult(value1,value2):
	Multiplication = value1 * value2
	return Multiplication

def Div(value1,value2):
	if value1 == value2 == 0:
		print("Division not possible")
	elif value2 == 0:
		print("Division is Infinity")
	else:
		Division = value1 / value2
		return Division


	
