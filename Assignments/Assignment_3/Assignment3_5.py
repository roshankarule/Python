from MarvellousNum import *


def ListPrime(value):
	temp = 0
	for i in range(len(value)):
		ans = ChkPrime(value[i])
		print(ans)
		temp = temp + ans
	return temp	
		

def main():
	size = 0
	Data = []
	size = int(input("Enter number of Elements : "))
	print("Enter the Elements : ")
	for i in range (size):
		Data.append(int(input()))
	print("Input Elements : ",Data)
	
	ret = ListPrime(Data)
	print("Sum of Prime Numbers is : ", ret)


if __name__ == "__main__":
	main()