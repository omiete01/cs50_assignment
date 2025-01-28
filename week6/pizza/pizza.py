# code to output a table formatted in ASCII ART

import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2: # exits code if the argument is less than 2
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2: # exits code if the argument is greater than 2
        sys.exit("Too many command-line arguments")
    else:

        csv_file = sys.argv[1]  
        if not (csv_file.endswith(".csv")): # exits code if the argument does not end with .csv
            sys.exit("Not a CSV file")
        else:
            print(format_table(csv_file)) # calling the format_table function and printing it out
            
            

def format_table(csv_doc):
    try:

        with open(csv_doc, newline="") as file:
            reader = csv.reader(file)  # reads each line of the file 
            # returns the file in a tabular grid format making the firstrow the header
            return tabulate(reader, headers="firstrow", tablefmt="grid")
        
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ in "__main__":
    main()

