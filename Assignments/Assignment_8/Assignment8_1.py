import os
import threading

def Even(no):
    x = 0
    print("Even Numbers: ")
    for i in range(0, no):
        if i%2 == 0 and i <= no:           
            
            print(i)

def Odd(no):
    y = 0
    print("Odd Numbers: ")
    for i in range(1, no):
        if i%2 != 0 and i <= no:
            y = (2 * i) - 1
            
            print(i)

def main():
    print("This program prints Even and Odd Numbers.")

    print("Enter the last number: ")
    no = int(input())


    thread1 = threading.Thread(target = Even, args = (no,))
    thread2 = threading.Thread(target = Odd, args = (no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()



if __name__ == "__main__":
    main()