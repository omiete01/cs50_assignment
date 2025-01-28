# this code removes all vowels from user input

def main():
    userinput = input("Input: ")
    print(shorten(userinput))

def shorten(word):

    for i in "aeiouAEIOU":
        word = word.replace(i, "")
    return word

if __name__ == "__main__":
    main()

