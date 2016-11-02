height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
BMI = 0

def calcBMI():
    global condition, BMI
    BMI = 703*(weight/(height**2))
    if BMI < 18.5:
        condition = "Underweight"
    elif BMI < 24.9:
        condition = "Normal"
    elif BMI < 29.9:
        condition = "Overweight"
    elif BMI < 34.9:
        condition = "Obese"
    elif BMI < 39.9:
        condition = "Very Obese"
    else:
        condition = "Morbidly Obese"
calcBMI()
print("Your BMI is:",BMI)
print("You are", condition,".")
