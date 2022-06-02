
def ChkNum(number):
	if number%2 == 0 :
		print("Even Number")
	else:
		print("Odd Number")


def main():
	no = int(input("Enter a Number : "))
	ans = ChkNum(no)


if __name__ == "__main__":
	main()