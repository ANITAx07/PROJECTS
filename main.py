import random
import string

def generate(length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters

    if numbers:
        characters += digits
    if special_char:
        characters += special

    password= ""
    meets_criteria = False
    has_number = False
    has_special = False        

    while not meets_criteria or len(password) < length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True 
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special
    return password         
password=generate(10)
print(password)

