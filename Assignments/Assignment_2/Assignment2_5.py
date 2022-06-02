
def Prime(x):
	temp = 0
	if x<=0:
		return "Enter a positive Number"
	elif x == 1:
		return "It is neither a prime nor a composite number"
	else:
		for i in range(1,x):
			if x%i == 0:
				temp = temp + i
				
	if temp == 1:
		return "It is a Prime Number"
	else:
		return "It is not a Prime Number"

def main():
	no = int(input("Enter a number : "))
	ret = Prime(no)
	print(ret)
	

if __name__ == "__main__":
	main()