class Circle:
    pi = 3.14

    def __init__ (self):
        self.radius = 0.0
        self.area = 0.0
        self.circumferance = 0.0

    def Accept(self,r):
        self.radius = r
        
    def CalculateArea(self):
        self.area = Circle.pi * self.radius * self.radius
                                
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.pi * self.radius

    def Display(self):
        
        print("The radius of Circle is: ",self.radius,"unit")

        Circle.CalculateArea(self)
        print("Area of Circle is: ",self.area, "sq. unit")

        Circle.CalculateCircumference(self)
        print("Circumference of Circle is: ",self.circumference,"units")
        
def main():
    print("Aim: To calculate Area and Circumference of Circle")

    print("Enter the radius of Circle: ",end = ' ')
    r = float(input())
    
    obj1 = obj2 = Circle()
    obj1.Accept(r)

    obj2.Display()
    
    
if __name__ == "__main__":
    main()