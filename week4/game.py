# guessing game

import random
import sys

while True:
    try:
        # asks user for level
        user_level = int(input("Input level: "))

        # raise value error if user input is a string
        if user_level == str:
            raise ValueError

        # checks if user input is less than 1 and prompts user again if it is
        if user_level < 1:
            pass
        else:

            # generates a random number between 1 and user input
            output = random.randint(1, user_level)

            while True:
                try:
                # asks the user to guess the generated number
                    rand_num = int(input("Guess: "))

                    # checks if the number is a string
                    if rand_num == str:
                        pass

                    # skips the loop if it is a negative number
                    if rand_num < 0:
                        continue

                    if rand_num > output:
                        print("Too large!")
                    elif rand_num < output:
                        print("Too small!")
                    elif rand_num == output:
                        print("Just right!")
                        # exits the program after the user guesses correctly
                        sys.exit()

                except ValueError:
                    pass

    except ValueError:
        pass


