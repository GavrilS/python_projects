"""
This is a tip calculator - you specify what percentage of the bill you want to leave as a 
tip and the calculator lets you know how much is that.

Usage:
    python calculate_tip.py

Notes:
    - the process asks the user for the total amount of the bill and also for the tip 
    percentage they want to leave behind
    - the process will also ask the user if they want to split the bill and if yes, between
    how many people and it will give out the amount each person needs to pay, assumming 
    the bill is to be split evenly between everyone

Example:
    Q -> What is the total bill: 188.90
    Q -> What is the tip percentage you want to leave: 5.50
    A -> Bill: 188.9
    A -> Tip percentage: 5.5
    A -> Total tip: 10.39
    A -> Total bill: 199.29
    Q -> Do you want to split the bill[yes|no]: yes
    Q -> Between how many people do you want to split the bill: 4
    A -> Everyone needs to pay 49.82
"""


def main():
    try:
        bill = round(float(input("What is the total bill: ")), 2)
        tip_percentage = round(float(input("What is the tip percentage you want to leave: ")), 2)

        tip = round(bill * tip_percentage / 100, 2)
        total_bill = round(bill + tip, 2)

        print(f"Bill: {bill};\nTip percentage: {tip_percentage};\nTotal tip: {tip};\nTotal bill: {total_bill}")

        split_bill = input("Do you want to split the bill[yes|no]: ")

        if 'yes' == split_bill.lower():
            split_between = int(input("Between how many people do you want to split the bill: "))
            split_bill = round(total_bill / split_between, 2)
            print(f"Everyone needs to pay {split_bill}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__=="__main__":
    main()