import os
import threading
from functools import reduce

def EvenList(value):
    ChkEven = lambda a : a%2 ==0
    newData = list(filter(ChkEven,value))
      
    Add = lambda a,b: a + b
    ans = reduce(Add,newData)
    print("Addition of Even Numbers in List is: ",ans)


def OddList(value):
    ChkOdd = lambda a : a%2 !=0
    newData = list(filter(ChkOdd,value))
      
    Add = lambda a,b: a + b
    ans = reduce(Add,newData)
    print("Addition of Odd Numbers in List is: ",ans)



def main():
    size = 0
    print("Enter length of List")
    size = int(input())

    Data = list()
    print("Enter Elements of List")
    for i in range(size):
        Data.append(int(input()))

    print(Data)
    
    thread1 = threading.Thread(target = EvenList, args = (Data,))
    thread2 = threading.Thread(target = OddList, args = (Data,))


    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()

    