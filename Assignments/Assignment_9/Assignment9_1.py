
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

    
    if (len(argv)==2):
        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage: Script is used to check if the file is present in current working directory.")
            exit()

        elif (argv[1] == "-h") or (argv[1] == "-H"):
            print("Help: Name_of_Script  First_Argument")
            print("First Argument: Filename.extension")
            exit()
    
    print("name of file to search: ", argv[1])
    path = os.getcwd()

    if (len(argv)==2):
        try: 
            if argv[1] in os.listdir(path):
                print("The file is present in the directory: "+path)
            else:
                print("The file is not present in the directory: "+path)

    
        except Exception:
            print("Exception while executing the script")
            print("please check the input or contact the developer")

    else:
        print("There is no such flag")
        exit()


    


#Starter of automation script
if __name__ == "__main__":
    main()