"""
Generate a list of number where every number that is divisible by 3 is replaced by the 
string 'fuzz', every number divisible by 5 is replaced by the string 'buzz' and every 
number divisible by both 3 and 5 is replaced by the string 'fuzzbuzz'. The user can supply 
the last number in a range starting from 0 or the computer will run the program with a 
default range of 100.

Usage:
    python fuzzbuzz.py 1000
"""
import sys


def main():
    upper_limit = 100
    try:
        if len(sys.argv) > 1:
            upper_limit = int(sys.argv[1])
    except Exception as e:
        print(f"Couldn't use the user input for range limit due to an error: {e}")
    
    print("The script is running with limit: ", upper_limit)

    for num in range(1, upper_limit + 1):
        div_by_three = num % 3 == 0
        div_by_five = num % 5 == 0

        if div_by_three and div_by_five:
            print("fuzzbuzz")
        elif div_by_three:
            print("fuzz")
        elif div_by_five:
            print("buzz")
        else:
            print(num)


if __name__=="__main__":
    main()