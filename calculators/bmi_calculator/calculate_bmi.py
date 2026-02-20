"""
The BMI calculator calculates the body mass index of an individual. BMI is a measurment of
a person's leanness or corpulence based on their height and weight, and is intended to
quantify tissue mass. It is widely used as an indicator of whether a person has a healthy
body weight for their height. More specifically, the value obtained from the BMI calculation
is used to categorize whether a person is underweight, normal weight, overweight or obese
depending on what range the value falls between.

Usage:
python calculate_bmi.py

Notes:
    - the script asks the user for their weight and height
    - the formula for calculating the BMI is weight / height**2

Example:
    - What is your weight (in kilograms): 80.5
    - What is your height (in meters): 1.80
    - Result:
        - Your BMI is 24.85
        - This BMI falls in the category of 'Normal' weight for adults age 20 or older
"""
BMI_CLASSIFICATION = {
    "Severe Thinness": "< 16",
    "Moderate Thinness": "16 - 17",
    "Mild Thinness": "17 - 18.5",
    "Normal": "18.5 - 25",
    "Overweight": "25 - 30",
    "Obese Class I": "30 - 35",
    "Obese Class II": "35 - 40",
    "Obese CLass III": "> 40"
}


def main():
    weight = round(float(input("What is your weight (in kilograms): ")), 2)
    height = round(float(input("What is your height (in meters): ")), 2)

    print("BMI Classification:\n", BMI_CLASSIFICATION)
    print("Weight: ", weight)
    print("Height: ", height)

    bmi = round(weight / height**2, 2)
    bmi_class = get_bmi_classification(bmi)

    print(f"Your BMI is {bmi}")
    print("Your BMI value is classified as", bmi_class)


def get_bmi_classification(bmi):
    if (bmi < 16):
        return "Severe Thinness"
    elif (bmi >= 16 and bmi < 17):
        return "Moderate Thinness"
    elif (bmi >= 17 and bmi < 18.5):
        return "Mild Thinness"
    elif (bmi >= 18.5 and bmi < 25):
        return "Normal"
    elif (bmi >= 25 and bmi < 30):
        return "Overweight"
    elif (bmi >= 30 and bmi < 35):
        return "Obese Class I"
    elif (bmi >= 35 and bmi < 40):
        return "Obese Class II"
    else:
        return "Obese Class III"


if __name__=="__main__":
    main()