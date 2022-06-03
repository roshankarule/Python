def Display(no, x):
    
    if x < no+1:
        print(x)
        x = x + 1
        Display(no,x)
    


def main():
    print("This program prints Forward Series")
    print("Enter a Number: ", end = ' ')
    num = int(input())
    Display(num, x = 1)
    

if __name__ == "__main__":
    main()