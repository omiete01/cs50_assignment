# this code removes all vowels from user input

userinput = input("Input: ")

for i in "aeiouAEIOU":
    # replaces every letter indicated in i above with nothing
    userinput = userinput.replace(i, "")

print(userinput)
