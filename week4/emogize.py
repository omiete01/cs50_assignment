# converting user words to emoji

import emoji

emogee = input("Input: ")

print(emoji.emojize(f"Output: {emogee}", language="alias"))
