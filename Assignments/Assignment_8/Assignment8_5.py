import os
import threading

def Forward(no):
    for i in range(1,no+1):
        print(i)

def Reverse(no):
    for i in range(no,0,-1):
        print (i)

def main():
    print("Enter a digit: ",end=' ')
    num = int(input())

    Thread1 = threading.Thread(target = Forward, args = (num,))
    Thread2 = threading.Thread(target = Reverse, args = (num,))

    print("Forward order: ")
    Thread1.start()
    Thread1.join()

    print("Reverse Order: ")
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()