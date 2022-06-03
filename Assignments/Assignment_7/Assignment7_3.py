def Display(no):
    if no > 0:
        print(no)
        no = no - 1
        Display(no)
    
def main():
    print("This program prints reverse Series")
    print("Enter a Number: ", end = ' ')
    num = int(input())
    Display(num)
    

if __name__ == "__main__":
    main()

    
