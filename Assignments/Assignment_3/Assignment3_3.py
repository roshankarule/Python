def Min(value):
	temp = value[0]
	for i in range(len(value)):
	
		if temp > value[i]:
			temp = value[i]
		else:
			temp = temp
	return temp


def main():
	size = 0
	Data = []
	size = int(input("Enter number of Elements : "))
	print("Enter the Elements : ")
	for i in range (size):
		Data.append(int(input()))
	print("Input Elements : ",Data)
	
	ret = Min(Data)
	print("Minimum value is : ", ret)


if __name__ == "__main__":
	main()