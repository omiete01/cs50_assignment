import sys
import csv

# expects 2 command-line argument: name of an existing csv file to read as input ,
# whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. 
# Assume that each student will have both a first name and last name.

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        
        # calling the function to clean the document
        write_to_file(sys.argv[1], sys.argv[2])

def write_to_file(before_csv, after_csv):
    # creating an empty list to save the cleaned document
    csv_list = []
    try:
        # makes sure the first document is a csv file
        if not(before_csv.endswith(".csv")):
            sys.exit("Not a csv file")

        with open(before_csv) as file:
            reader = csv.DictReader(file)

            for line in reader:
                # splitting the name row into first and last name
                last, first = line["name"].split(", ") 
                house = line["house"]
                # updating the list with the declared variables
                csv_list.append({"first": first, "last": last, "house": house}) 

            with open(after_csv, "w") as file2:
                # setting the fieldnames of the new document
                writer = csv.DictWriter(file2, fieldnames= ["first", "last", "house"]) 
                writer.writeheader()
                return writer.writerows(csv_list)
            
    except FileNotFoundError:
        sys.exit(f"Could not read {before_csv}")
    

if __name__ in "__main__":
    main()
