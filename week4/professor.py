# generates random math additions and prompts user to answer

import random

def main():

    wrong = 0
    total_problems = 10
    trys = 0

    # declaring a variable for the function get_level()
    level = get_level()

    # looping through a range of 10 total problems as declared
    for _ in range(total_problems):

        # declaring variables for the returned values from generate_integer() function
        number1, number2 = generate_integer(level)
        operator = "+"

        # displays a random math expression using the values from generate_integer() function
        expr = str(number1) + " " + operator + " " + str(number2)

        # adds up the generated numbers and store them in the answer variable
        answer = int(number1) + int(number2)

        while True:
            guess = input(f"{expr} = ")

            # if users guess does not equal the answer, it displays EEE and reprompts user again,
            # each time adding 1 to the number of attempts
            # if users guess equals answer, it moves on to the next expression

            if guess != str(answer):
                print("EEE")
                trys += 1

                # displays answer if users guess is wrong 3 times and moves on to the next question
                if trys == 3:

                    print(f"{expr} = {answer}")
                    wrong += 1
                    break

            elif guess == str(answer):
                # restart the number of attempts and breaks out of the loop once the answer is correct
                trys = 0
                break

    print(f"Score: {10 - wrong}")

def get_level():

    while True:
        try:
            level = int(input("Level: "))

            # checks if user input numbers 1 to 3 and reprompts if user doesn't. returns user input
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):

    # randomly generates numbers from 1 to 9, 10 to 99 and 100 to 999 of returned
    # value from get_level() function

    if level == 1:
        min_num = random.randint(0, 9)
        max_num = random.randint(0, 9)
    elif level == 2:
        min_num = random.randint(10, 99)
        max_num = random.randint(10, 99)
    elif level == 3:
        min_num = random.randint(100, 999)
        max_num = random.randint(100, 999)

    return min_num, max_num

if __name__ == "__main__":
    main()

