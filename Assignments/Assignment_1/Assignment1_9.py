def EvenNo(y):
	for i in range(1,y):
		if (i%2 == 0):
			print(i)
		i = i + 2	

def main():
	no = int(input("How many Even Numbers :"))
	x = (2*no)+1
	display = EvenNo(x)



if __name__ == "__main__":
	main() 