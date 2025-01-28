# This code converts textlike emoticons to emojis

userinput = input("")
emoticon1 = ":)"
emoticon2 = ":("

def convert():
    smileyface = "🙂"
    frowneyface = "🙁"
    print(userinput.replace(emoticon1, smileyface).replace(emoticon2, frowneyface))

def main():

    convert()


main()
