

Multiply = lambda a,b : a*b

def main():
    print("Enter First Number : ",end=' ')
    no1 = int(input())
    print("Enter Second Number : ",end=' ')
    no2 = int(input())

    ret = Multiply(no1,no2)
    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()

