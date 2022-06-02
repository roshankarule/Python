def Factors(x):
	temp = 0
	if x <= 0:
		return "Factors not possible"
	else:
		for i in range(1,x):
			if x%i == 0:
				temp = temp + i
				
		return temp


def main():
	no = int(input("Enter a Number : "))
	ret = Factors(no)
	print("Sum of Factors is : ", ret)


if __name__ == "__main__":
	main()