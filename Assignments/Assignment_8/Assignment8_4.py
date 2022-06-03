import os
import threading


def small(value):
    count = 0
    print("lowercase characters: ", end=' ')
    for i in value:
        if i in lower:
            count += 1
            print(i, end=' ')
    print("")
    print("Lowercase Count:",count)


def capital(value):
    count = 0
    print("uppercase characters: ", end=' ')
    for i in value:
        if i.isupper():
            count += 1
            print(i, end=' ')
    print("")
    print("Uppercase Count:",count)


def digits(value):
    count = 0
    print("Numeric characters: ", end=' ')
    for i in value:
        if i.isnumeric():
            count += 1
            print(i, end=' ')
    print("")
    print("Numeric Count:",count)


def main():
    '''This Program returns count of lowercase, uppercase characters and digits
        as output.
    '''

    print("Enter a String: ",end=' ')
    data = input()

    lowercase = threading.Thread(target = small, args = (data,))
    uppercase = threading.Thread(target = capital, args = (data,))
    number = threading.Thread(target = digits, args = (data,))

    lowercase.start()
    uppercase.start()
    number.start()

    lowercase.join()
    uppercase.join()
    number.join()


if __name__ == "__main__":

    lower = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    main()

