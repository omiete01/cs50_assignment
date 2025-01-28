# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively.

def main():
    greeting = input("Greeting: ")
    if greeting.casefold().strip().startswith("hello"):
        print("$0")
    elif greeting.casefold().strip().startswith("h"):
        print("$20")
    else:
        print("$100")

# casefold method removes case distinctions in the string
# strip removes whitespaces in the string
# while startswith method returns True if the string starts with "hello

main()
