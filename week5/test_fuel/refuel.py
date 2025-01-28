# rewriting the fuel code to use pytest 

def main():
    fraction = input("Fraction: ")
    n = convert(fraction)
    print(gauge(n))

def convert(fraction):

    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError

    return round((x / y) * 100) 

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

