# this is a code that prompts the user for an answer to the Great Question of Life, the Universe and Everything

# defining the main function where the main code will run
def main():
    question = input("What is the Great Question of Life, the Universe and Everything? ")
    # casefold method removes case distinctions in the string
    # strip method removes whitespaces in the string
    question = question.casefold().strip()
    answer(question)

# defining the answer to the question in a function to be used in the main function
def answer(q):
    if q == "42" or q == "forty-two" or q == "forty two":
        print("Yes")
    else:
        print("No")

# calling the main function
main()


