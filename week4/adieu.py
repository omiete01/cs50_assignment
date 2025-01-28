# this program takes in user input in a list and greets them goodbye

import inflect

# creating an instance of inflect
p = inflect.engine()

""" this is a docstring """

def main():
    # creating an empty list to store the names
    names = []
    while True:
        try:
            name = input("Name: ")
            # adding names to the list
            names.append(name)
            # joining the names, seperating them by commas and the last one "and"
            join_names = p.join(names)
        except EOFError:
           
            print(f"Adieu, adieu, to {join_names}")
            break


main()
