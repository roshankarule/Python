from functools import reduce

def ChkPrime(no):
    temp = 0
    if no <= 0:
        return False
    elif no == 1:
        return False
    else:
        for i in range(1,no):
            if no % i == 0:
                temp = temp + i
			
    if temp == 1:
        return True
    else:
        return False
        
Multiply = lambda no : no * 2

Maximum = lambda a,b : max(a,b)


def main():
    size = 0
    data = []
    print("Enter no of Elements in List : ", end=' ')
    size=int(input())
    print("Enter the Elements :")
    for i in range(size):
        data.append(int(input()))

    print("Input list : ",data)

    newData = list(filter(ChkPrime,data))
    print("List after Filter : ",newData)

    Mult = list(map(Multiply, newData))
    print("List after map : ",Mult)

    ret = reduce(Maximum,Mult)
    print("Output after reduce : ",ret)

if __name__ == "__main__":
    main()
