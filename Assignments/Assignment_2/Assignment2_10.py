
def Addition(value):
	sum = 0
	for i in range (len(value)):
		sum = sum + value[i]
	return sum


def number(value):
	size = 0
	Data = []
	size = len(value)
	for i in range (size):
		Data.append(int(value[i]))
	
	ans = Addition(Data)
	return ans


def main():
	no = input("Enter a Number : ")
	ret = number(no)
	print(" The sum of digits is : ",ret)



if __name__ == "__main__":
	main()