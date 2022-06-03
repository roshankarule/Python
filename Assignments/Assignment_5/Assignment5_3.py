class Arithmetic:

    def __init__(self):
        self.value1 = 0.0
        self.value2 = 0.0

    def Accept(self,x ,y):
        self.value1 = x
        self.value2 = y

    def __Addition(self):
        self.add = self.value1 + self.value2
    
    def __Substraction(self):
        self.sub = self.value1 - self.value2

    def __Multiplication(self):
        self.mul = self.value1 * self.value2

    def __Division(self):
        if self.value2 !=0:
            self.div = self.value1 / self.value2
        else:
            self.div = "Not Possible"

    def Display(self):
        Arithmetic.__Addition(self)
        print("The Addition is: ",self.add)

        Arithmetic.__Substraction(self)
        print("The Substraction is: ",self.sub)

        Arithmetic.__Multiplication(self)
        print("The Multiplication is: ",self.mul)

        Arithmetic.__Division(self)
        print("The Division is: ",self.div)


def main():
    print("Enter first Number: ",end = ' ')
    x = float(input())
    print("Enter second Number: ",end = ' ')
    y = float(input())
    print(" ")
    obj1 = Arithmetic()

    obj1.Accept(x,y)
    obj1.Display()


if __name__ == "__main__":
    main()