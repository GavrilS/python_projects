"""
The script generates a password which satisfies the following requirements:
    - minimum length is 10 characters
    - should contain at least 2 letters from the latin alphabet - lower and upper case both 
    work
    - should contain at least 2 special characters
    - should contain at least 6 diggits from 0 to 9
    - maximum length allowed is 20 characters

The user can provide as an argument to the script the number of character the password 
should be. This number must be between 10 and 20 (inclusive). If the user provides an 
invalid character count, the default of 10 would be used.

Usage:
    python generate_password.py 20
"""
import sys
import random

ALPHABET_CHARACTERS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
    "S", "T", "U", "V", "W", "X", "Y", "Z", "a", 
    "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", 
    "t", "u", "v", "w", "x", "y", "z"
]
alphabet_left = 2
ALPHABET_MIN = 2
ALPHABET_LENGTH = len(ALPHABET_CHARACTERS)

SPECIAL_CHARACTERS = [
    "!", "@", "#", "$", "%", "^", "&", "*", ")", "+", "(", "/", "|"
]
special_characters_left = 2
SPECIAL_CHARACTERS_MIN = 2
SPECIAL_CHARACTERS_LENGTH = len(SPECIAL_CHARACTERS)

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_left = 6
NUMBERS_MIN = 6
NUMBERS_LENGTH = len(NUMBERS)

CATEGORIES = {
    0: {
        "list_item": ALPHABET_CHARACTERS,
        "char_left": alphabet_left,
        "char_min": ALPHABET_MIN,
        "list_len": ALPHABET_LENGTH
    },
    1: {
        "list_item": SPECIAL_CHARACTERS,
        "char_left": special_characters_left,
        "char_min": SPECIAL_CHARACTERS_MIN,
        "list_len": SPECIAL_CHARACTERS_LENGTH
    },
    2: {
        "list_item": NUMBERS,
        "char_left": numbers_left,
        "char_min": NUMBERS_MIN,
        "list_len": NUMBERS_LENGTH
    }
}
TOTAL_MIN_CHARACTERS = 10


def main():
    password_length = 10
    try:
        if len(sys.argv) > 1:
            user_password_length = int(sys.argv[1])
            if user_password_length > password_length and user_password_length <= 20:
                password_length = user_password_length
            else:
                print(f"The provided password length {user_password_length} is not allowed... Will run with the default length!")
    except Exception as e:
        print(f"Got an error trying to get the password length set by the user: {e}")
        # print(f"Running with the default password length: {password_length}")
    # print(f"Password length will be {password_length}")
    flag = True
    actual_password = ""
    min_characters_left = TOTAL_MIN_CHARACTERS
    while flag:
        category = CATEGORIES[random.randint(0, 2)]
        if category["char_left"] <= 0:
            if (password_length - len(actual_password)) > min_characters_left:
                # can add password
                actual_password, min_characters_left = add_character_to_password(actual_password, category, min_characters_left, update_min_characters=False)
            else:
                continue
        else:
            actual_password, min_characters_left = add_character_to_password(actual_password, category, min_characters_left, update_min_characters=True)
        
        if password_length == len(actual_password):
            flag = False
    
    print("Your password is: ", actual_password)


def add_character_to_password(password, category, total_min_characters, update_min_characters=True):
    # print("Category: ", category)
    character_position = random.randint(0, category["list_len"] - 1)
    password += category["list_item"][character_position]
    if update_min_characters:
        total_min_characters -= 1
        category["char_left"] -= 1
    # print("Total min characters left: ", total_min_characters)
    # print("Password: ", password)
    # print("Password length: ", len(password))
    # print("Category: ", category)
    # print("*" * 100)

    return (password, total_min_characters)


if __name__=="__main__":
    main()
