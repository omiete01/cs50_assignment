# assignment week 1
# a code to check meal time

'''
If up for a challenge, optionally add support for 12-hour times, allowing the user to 
input times in these formats too:

#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.
'''


def main():
    meal_time = input("What time is it? ")
    # rem_suf(meal_time)
    if convert(meal_time) >= 7.00 and convert(meal_time) <= 8.00:
        print("breakfast time")
    elif convert(meal_time) >= 12.00 and convert(meal_time) <= 13.00:
        print("lunch time")
    elif convert(meal_time) >= 18.00 and convert(meal_time) <= 19.00:
        print("dinner time")



def convert(time):
    # time = time.strip("a.m.")
    # time = time.strip("p.m.")
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    total_time = hours + minutes / 60

    return total_time

# def rem_suf(suff):
#     if suff.endswith("a.m."):
#         suff.removesuffix
#     elif suff.endswith("p.m."):
#         suff.removesuffix
#     return suff


if __name__ == "__main__":
    main()

