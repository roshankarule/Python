def Summation(x):
    size = len(x)

    def Addition(x,size, y):
        if 0 < size:
            y = y + x[size - 1]
            size = size - 1
            
            if size == 0:
                print("The addition of digits is: ", y)
            else:
                Addition(x,size,y)
        
    Addition(x, size, y=0)
    

def Arrange(value,length):
    size = length
    Data = []
    value = value
    
    def Number(Data,value,size):
        if 0 < size:
            Data.append(int(value[size-1]))
            size = size - 1
            Number(Data,value,size)

        return Data

    num = Number(Data,value,size)
    Summation(num)


def main():
    print("This program returns the addition of digits")
    print("Enter a Number: ",end=' ')
    num = input()
    size = len(num)
    
    Arrange(num, size)


if __name__ == "__main__":
    main()