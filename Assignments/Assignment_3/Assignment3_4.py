def Frequency(value):
	no = int(input("Enter an element in Data : "))
	temp = 0
	for i in range(len(value)):
		if value[i] == no:
			temp = temp + 1
					
	return temp


def main():
	size = 0
	Data = []
	size = int(input("Enter number of Elements : "))
	print("Enter the Elements : ")
	for i in range (size):
		Data.append(int(input()))
	print("Input Elements : ",Data)
	
	ret = Frequency(Data)
	print("Frequency of Element is : ", ret)


if __name__ == "__main__":
	main()