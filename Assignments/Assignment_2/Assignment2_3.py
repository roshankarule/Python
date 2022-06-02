def Factorial(x):
	temp = 1
	if x == 0:
		return 1
	elif x < 0:
		return "Not possible. Enter a positive Number."
	else:
		for i in range(x,0,-1):
			temp = temp*i
		return temp
		
def main():
	no = int(input("Enter a Number : "))
	ret = Factorial(no)
	
	print("The Facrotial is : ",ret)
	
if __name__ == "__main__":
	main()