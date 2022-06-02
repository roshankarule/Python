from Arithmatic import *

def main():
	no1 = 0
	no2 = 0
	no1 = int(input("Enter The first Number : "))
	no2 = int(input("Enter the Second Number : "))
	
	Addition = Add(no1,no2)
	print("Addition is : ",Addition)
	Substraction = Sub(no1,no2)
	print("Substraction is : ", Substraction)
	Multiplication = Mult(no1,no2)
	print("Multiplication is : ", Multiplication)
	Division = Div(no1, no2)
	if no2 == 0:
		print(" ")
	else:
		print("Division is : ", Division)

if __name__ == "__main__":
	main()
