def Display(x):
	if x > 0:
		for i in range(x):
			for i in range(x):
				print("*",end=' ')
			x = x - 1
			print()
	else:
		print("Enter a Positive Integer.")

def main():
	no = int(input("Enter a Number : "))
	Display(no)


if __name__ == "__main__":
	main()