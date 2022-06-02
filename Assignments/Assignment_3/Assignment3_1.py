def Addition(value):
	add = 0
	for i in range(len(value)):
		add = add + value[i]
	return add


def main():
	size = 0
	Data = []
	size = int(input("Enter number of Elements : "))
	print("Enter the Elements : ")
	for i in range (size):
		Data.append(int(input()))
	print("Input Elements : ",Data)
	
	ret = Addition(Data)
	print("Addition is : ", ret)


if __name__ == "__main__":
	main()