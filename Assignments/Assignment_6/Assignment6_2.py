class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self,value1):
        self.Amount = self.Amount + value1

    def Withdraw(self,value2):
        self.Amount = self.Amount - value2

    def CalculateInterest(self):
        self.Interest = (self.Amount * 1 * BankAccount.ROI) / 100

    def Display(self):
        print("Name of Account Holder: ",self.Name)
        print("Account Balance: ", self.Amount)

        print("Interest on Balance: ", self.Interest)

def main():
    print("Welcome to the Bank.")

    obj1 = BankAccount("Thor",0)
    obj1.Deposit(10000)
    obj1.Withdraw(100)
    obj1.CalculateInterest()

    obj2 = BankAccount("Zeus",10000)
    obj2.Deposit(50000)
    obj2.Withdraw(1000)
    obj2.CalculateInterest()

    obj1.Display()
    obj2.Display()

if __name__ == "__main__":
    main()