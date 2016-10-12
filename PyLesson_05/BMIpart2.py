height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
BMI = 703*(weight/(height**2))

def calcBMI():
    if BMI < 18.5:
        return "Underweight"
    elif BMI < 24.9:
        return "Normal"
    elif BMI < 29.9:
        return "Overweight"
    elif BMI < 34.9:
        return "Obese"
    elif BMI < 39.9:
        return "Very Obese"
    else:
        return "Morbidly Obese"
print("Your BMI is:",BMI)
print("You are", calcBMI(),".")
