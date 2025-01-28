# This is a code that converts that converts mass to joules

mass = int(input("m: "))

def convert():
    # we are using e=mc2 to convert mass to joules where c is the speed of light
    c = 3 * 10**8
    energy = mass * (c**2)
    print("E:", energy)

convert()
