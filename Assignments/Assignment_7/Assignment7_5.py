def Factorial(no , x, y):
    if no == 0:
        print(no,"! =",y)

    elif no >= x:
        y = y * x
        x = x + 1
        Factorial(no, x, y)

    else:
        print(no,"! =",y)
    

def main():
    print("This program prints factorial.")
    print("Enter a Number: ", end = ' ')
    num = int(input())
    Factorial(num, x = 1, y = 1)
    
    
if __name__ == "__main__":
    main()