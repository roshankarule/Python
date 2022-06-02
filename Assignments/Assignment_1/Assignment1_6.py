def integer(no):
	
	if no < 0:
		print("Negative Integer.")
	elif no == 0:
		print("Zero.")
	else:
		print("Positive Integer.")


def main():
	value = int(input("Enter an integer : "))
	ans = integer(value)


if __name__ == "__main__":
	main()