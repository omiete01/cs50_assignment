# This is a code that calculates the percentage of your meals cost

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # calculates the tip amount
    tip = dollars * percent
    # prints out the rounded result to two decimals
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.removeprefix("$")
    d = float(d)
    return d

def percent_to_float(p):
    p = p.removesuffix("%")
    p = float(p) / 100
    return p

main()
