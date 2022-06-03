from functools import reduce

ChkNum = lambda no : 90 >= no >= 70
Inc = lambda no : no + 10
Multiply = lambda a,b : a * b


def main():
    size = 0
    data = []
    print("Enter no of Elements in List : ", end=' ')
    size=int(input())
    print("Enter the Elements :")
    for i in range(size):
        data.append(int(input()))

    print("Input list : ",data)

    newData = list(filter(ChkNum,data))
    print("List after Filter : ",newData)

    IncrementedData = list(map(Inc,newData))
    print("List after map : ",IncrementedData)

    ret = reduce(Multiply, IncrementedData)
    print("Output after reduce : ",ret)

if __name__ == "__main__":
    main()
