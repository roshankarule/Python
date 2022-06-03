
#Import statements if necessary
from sys import *
import os


#Entry Point of Script
def main():
    print("------------Automation-------------")
   
    
    if (len(argv) > 2) or (len(argv) < 1):
        print("Invalid number of Argumnets")
        print("Suggestion: use -h for help or -u for usage")
        exit()

    
    if (len(argv)==1):
        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage: Script is used compare two files in current working directory.")
            exit()

        elif (argv[1] == "-h") or (argv[1] == "-H"):
            print("Help: Name_of_Script  First_Argument ")
            print("First Argument: Filename.extension")
            exit()
    
    print("string to search: ")
    string = input()
    cnt = 0
    line_no = 0

    path = os.getcwd()

    if (len(argv)==1):
        try: 
            if os.path.exists(argv[1]):
                data = open(argv[1],"r")
                content = data.read()

                for line in content:
                    line_no += 1

                    if string in line:
                        cnt += 1
                        print("The string is repeated times",cnt)

            exit()                


        
        except Exception:
            print("Exception while executing the script")
            print("please check the input or contact the developer")
            exit()
    

#Starter of automation script
if __name__ == "__main__":
    main()