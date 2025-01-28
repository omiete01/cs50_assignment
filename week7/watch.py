# this code extracts youtube links and convert them to shorter shareable urls

import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # searches for youtube links
    if match := re.search(r'src="http(s)?://(www\.)?youtube\.com/embed/([0-9a-zA-Z]+)"', s):
        return f"https://youtu.be/{match.group(3)}"

if __name__ == "__main__":
    main()