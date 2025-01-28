# checks validity of number plates


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): # defining a function that takes in an argument

    # ensures vanity plates start with at least 2 letters
    if not (2 < len(s) < 7):
        return False

    # checks if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # checks if there are any digits in plates except for the last character
    if '0' in s and s.index('0') < len(s) - 1:
        return False

    # Checks if the first number is not '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            break
        break

    return True

main()
