
SqNum = lambda a : a**2

def main():
    print("Enter a Number: ",end = ' ')
    data = []
    (data.append(int(input())))
    
    ret = map(SqNum,data)
    print("The square of Number is : ",ret)

if __name__ == "__main__":
    main()