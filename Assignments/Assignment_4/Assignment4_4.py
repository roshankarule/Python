from functools import reduce

ChkEven = lambda no : no % 2 == 0
NumSq = lambda no : no ** 2
Add = lambda a,b : a + b


def main():
    size = 0
    data = []
    print("Enter no of Elements in List : ", end=' ')
    size=int(input())
    print("Enter the Elements :")
    for i in range(size):
        data.append(int(input()))

    print("Input list : ",data)

    newData = list(filter(ChkEven,data))
    print("List after Filter : ",newData)

    SqData = list(map(NumSq,newData))
    print("List after map : ",SqData)

    ret = reduce(Add, SqData)
    print("Output after reduce : ",ret)

if __name__ == "__main__":
    main()
