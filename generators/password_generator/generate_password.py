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
alphabet_length = len(ALPHABET_CHARACTERS)

SPECIAL_CHARACTERS = [
    "!", "@", "#", "$", "%", "^", "&", "*", ")", "+", "(", "/", "|"
]
special_characters_left = 2
special_characters_length = len(SPECIAL_CHARACTERS)

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_left = 6
numbers_length = len(NUMBERS)



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
    print(f"Password length will be {password_length}")
    flag = True
    while flag:
        pass


if __name__=="__main__":
    main()
