# this code converts 12hr time format to 24hr time format using regex

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    pattern = r"(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + pattern + " to " + pattern + "$", s)
    if match:
        before = convert_time(match.group(1), match.group(2), match.group(3))
        after = convert_time(match.group(4), match.group(5), match.group(6))
        return f"{before} to {after}"
    else:
        raise ValueError


def convert_time(hour, min, am_pm):
    if am_pm == "PM" and hour != "12":
        hour = f"{int(hour)+12:02}"
      
    elif am_pm == "AM" and hour == "12":
        hour = 0
    
    if am_pm == "AM":
        hour = f"{int(hour):02}"

    if min == None:
        min = 00
        min = int(min)
    return f"{hour}:{min:02}"

if __name__ == "__main__":
    main()
