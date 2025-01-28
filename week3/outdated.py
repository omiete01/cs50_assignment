# converting date to format yyyy-mm-dd

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
    
        try:
            # makes sure user input is in the format month day, year or month/day/year
            date = input("date: ")

            if "," in date:
                # seperates user input to 3 variables where x is month, y is day and z is year
                x,y,z = date.split()
                # checks if x is in the list(month)
                month_item = month.index(x)
                if x in month:
                    # adds 1 to the index of x in the list and formats it with a leading 0
                    format_x = f"{month_item + 1:02}"
                else:
                    raise ValueError
                
                # converts y to integer after stripping it of comma
                y = int(y.strip(","))
                # checks if y is between 1 and 32 excluding 32
                if y in range(32):
                    # formats y with a leading 0
                    format_y = f"{y:02}"
                else:
                    raise ValueError
                
                # checks if z is a 4 digit number
                if len(z) == 4 and z.isdigit():
                    print(f"{z}-{format_x}-{format_y}")
                    break
                else:
                    raise ValueError
                               
            elif "/" in date:

                # seperates user input to 3 variables where x is month, y is day and z is year
                x,y,z = date.split("/")
                
                x = int(x)
                # checks if x is in range 13 and formats it with leading 0
                if x in range(13):
                    format_x = f"{x:02}"
                else:
                    raise ValueError
                
                y = int(y)
                # checks if y is in range 32 and formats it with leading 0
                if y in range(32):
                    format_y = f"{y:02}"
                else:
                    raise ValueError
                
                # checks if z is a 4 digit number
                if len(z) == 4 and z.isdigit():
                    print(f"{z}-{format_x}-{format_y}")
                    break
                else:
                    raise ValueError
                
            else:
                raise ValueError
        except ValueError:
            pass


main()
