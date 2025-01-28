# dictionary assignment

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    # declaring the total variable at $0
    total = 0.0

    while True:
        try:
            # asks user for input and titlecase it
            item = input("Item: ").title()

            if item in menu:
                # adds the price of user input to the total variable
                total = total + menu[item]
                # formats the output to two decimal places
                print(f"Total: ${total:.2f}")
            else:
                continue
        except KeyError:
            # ignores key errors
            pass
        except EOFError:
            # stops the program when user inputs control z
            break

main()

