#### convert user input to figlet

# importing usable modules
import random
import sys
from pyfiglet import Figlet

def main():

    # exits the program if the length of sys.argv is not 1 or 3
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        pass
    else:
        sys.exit("Invalid number of arguments")

    # creating an instance of Figlet
    fig  = Figlet()

    # converts user input to a random font if there is no argument
    if len(sys.argv) == 1:
        user_input = input("Input: ")
        fonts = fig.getFonts()
        random_font = random.choice(fonts)
        figlet = Figlet(font=random_font)
        new_font = figlet.renderText(user_input)
        print(f"Output: \n{new_font}")

    # converts user input to a specified font if there are 3 arguments
    elif len(sys.argv) == 3:

        # declaring the argument as variables 
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        if arg1 in ["-f", "--font"] and arg2 in fig.getFonts(): 
            user_input = input("Input: ")
            fig.getFonts()
            figlet = Figlet(font=arg2)
            new_font = figlet.renderText(user_input)
            print(f"Output: \n{new_font}")
        else:
            sys.exit("Invalid Usage")

       

main()
