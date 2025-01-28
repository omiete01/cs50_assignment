# a script to count the lines of code. it excludes blank lines and comments. 
# this script takes in command-line arguments with python files

import sys

def main():
    if len(sys.argv) < 2: # exits code if the argument is less than 2
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2: # exits code if the argument is greater than 2
        sys.exit("Too many command-line arguments")
    else:

        lines = sys.argv[1]  
        if not (lines.endswith(".py")): # exits code if the argument does not end with .py
            sys.exit("Not a Python file")
        else:
            # calling the function on the variable assigned to the command-line argument
            print(count_lines_of_code(lines))

def count_lines_of_code(filename):
    try:
        count = 0
        with open(filename, "r") as file:
            line = file.readlines()  # reading the file and storing it in a variable
            for i in line:  # looping through each line
                # checks if the lines has a leading whitespace or starts with the # symbol. 
                # increments the count variable by 1 if it does not
                if not(i.strip() == "" or i.lstrip().startswith("#")): 
                    count += 1
            return count # returns the count value
    except FileNotFoundError:  # exits code if the file is not found
        sys.exit("File does not exist")

if __name__ in "__main__":
    main()