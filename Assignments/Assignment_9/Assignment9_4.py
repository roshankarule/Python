
#Import statements if necessary
from sys import *
import os
import hashlib

#Entry Point of Script
def main():
    print("------------Automation-------------")
   
    
    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid number of Argumnets")
        print("Suggestion: use -h for help or -u for usage")
        exit()

    
    if (len(argv)==2):
        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage: Script is used compare two files in current working directory.")
            exit()

        elif (argv[1] == "-h") or (argv[1] == "-H"):
            print("Help: Name_of_Script  First_Argument Second_Argument")
            print("First Argument: Filename.extension")
            print("Second Argument: Filename.extension")
            exit()
    
    print("name of file to compare: ", argv[1], argv[2])
    path = os.getcwd()

    if (len(argv)==3):
        try: 
            if os.path.exists(argv[1]):
                
                file1 = open(argv[1], 'rb')
                x = file1.read()
                ahash = hashlib.md5(x)
                print(str(ahash.hexdigest()))

            if os.path.exists(argv[2]):
                
                file2 = open(argv[2], 'rb')
                y = file2.read()
                bhash = hashlib.md5(y)
                print(str(bhash.hexdigest()))

            if ahash != bhash:
                print("Files are not Identical.")
                
            else:
                print("Files are Identical.")

            exit()                


        
        except Exception:
            print("Exception while executing the script")
            print("please check the input or contact the developer")
            exit()
    

#Starter of automation script
if __name__ == "__main__":
    main()