import re

# implement a function that counts the number of times 'um' appears in the text, case-insensitively,
# as a word, not a substring of another word

def main():
    print(count(input("Text: ")))

# function to count the number of "um" found in a text
def count(s):
    count = 0
    # ensures to count "um" a word and not as a substring
    # "\bum\b" matches only individual "um"
    pattern = r"\bum\b"
    match = re.findall(pattern, s, re.IGNORECASE)
    # loops through each match and increment the count by 1 when a match is found
    for _ in match:
        count += 1
    return count

if __name__ == "__main__":
    main()