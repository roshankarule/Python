class Numbers:

    temp = 0

    def __init__(self,value):
        self.value = value

    def Factors(self):
        if self.value < 1:
            print ("Enter a valid Number")
        
        else:
            print("The Factors are: ",end =' ')
            for i in range(1,self.value):
                if self.value % i == 0:
                    Numbers.temp = Numbers.temp + i
                    print(i,"x",end=' ')
            print(self.value)

    def ChkPrime(self):
        if self.value < 1:
            print("Enter a valid Number")
        elif self.value == 1:
            print("Neither Prime nor Composite")
        elif Numbers.temp == 1:
            print ("It is a Prime Number")
        else: 
            print("It is not a Prime Number")

    def SumFactors(self):
        if self.value < 1:
            print("Enter a valid Number")
        else:
            print("The Sum of Factors is: ",Numbers.temp)

    def ChkPerfect(self):
        if self.value < 1:
            print("Enter a valid Number")
        elif Numbers.temp == self.value:
            print ("It is a Perfect Number.")
        else:
            print ("It is NOT a perfect Number")



def main():
    print("Enter any Number: ",end=' ')
    x = int(input())
        
    obj1 = Numbers(x)

    obj1.Factors()
    obj1.SumFactors()
    obj1.ChkPrime()
    obj1.ChkPerfect()
    
    
if __name__ == "__main__":
    main()