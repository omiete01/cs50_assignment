# this code validates email address using validators
from validator_collection import validators, errors

email = input("What's your email address? ")

try:
    if validators.email(email):
        print ("Valid")
except errors.InvalidEmailError:
    print ("Invalid")
