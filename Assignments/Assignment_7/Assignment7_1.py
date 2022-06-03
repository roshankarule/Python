def display(no):
    if 0 < no:
        print("*",end=' ')
        no = no - 1
        display(no)

def main():
    num = int(input("Enter a Number: "))
    display(num)

if __name__ == "__main__":
    main()