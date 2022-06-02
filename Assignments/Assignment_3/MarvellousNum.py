
def ChkPrime(x):
	set = 0
	if x<=0:
		return 0
	elif x == 1:
		return 0
	else:
		for i in range(1,x):
			if x%i == 0:
				set = set + i
		if set == 1:
			return x
		else:
			return 0

