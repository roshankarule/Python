import os
import threading

def EvenFactor(no):
    temp = 0
    if no < 1:
        print ("Enter a valid Number")
    
    else:
        for i in range(1,no):
            if no % i == 0:
                if i % 2 == 0:
                    temp = temp + i
        
        print("Sum of Even Factors is: ", temp)
        

def OddFactor(no):
    temp = 0
    if no < 1:
        print ("Enter a valid Number")
    
    else:
        for i in range(1,no):
            if no % i == 0:
                if i % 2 != 0:
                    temp = temp + i
                    
        print("Sum of Odd Factors is: ", temp)
        


def main():
    """This program prints the addition of Even and Odd Factors."""

    print("Enter a NUmber: ", end =' ')
    num = int(input())

    EvenSum = threading.Thread (target = EvenFactor, args = (num,))
    OddSum = threading.Thread (target = OddFactor, args = (num,))

    EvenSum.start()
    OddSum.start()

    EvenSum.join()
    OddSum.join()

    print("Exit from Main")


if __name__ == "__main__":
    main()