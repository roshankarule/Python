def Add(value1, value2):
	Addition = value1 + value2
	return Addition
	
def main():
	no1 = int(input("Enter the First Number : "))
	no2 = int(input("Enter the Second Number : "))
	ans = Add(no1,no2)
	
	print("Addition of two Numbers is :", ans)
	

if __name__ == "__main__":
	main()