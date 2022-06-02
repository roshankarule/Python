
def Display(value):
		for i in range(value):
			print("*", end=' ')


def user():
	no = int(input("Enter Number of times to Display * :"))
	ret = Display(no)

if __name__ == "__main__":
	user()