def Display(x):
	if x > 0:
		for i in range(1,x+1):
			for j in range(1,x+1):
				print(j,end=' ')
			print()
	else:
		print("Enter a Positive Integer.")

def main():
	no = int(input("Enter a Number : "))
	Display(no)


if __name__ == "__main__":
	main()