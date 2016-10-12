grade1 = input("Enter your math grade: ")
grade2 = input("Enter your science grade: ")
grade3 = input("Enter your English grade: ")
grade4 = input("Enter your history grade: ")
grade5 = input("Enter your Spanish grade: ")
grade6 = input("Enter your computer grade: ")
grade7 = input("Enter your government grade: ")

def calcPoint(grade):
    if grade == "A":
        return 4.0
    if grade == "B":
        return 3.0
    if grade == "C":
        return 2.0
    if grade == "D":
        return 1.0
    if grade == "F":
        return 0
math = calcPoint(grade1)
science = calcPoint(grade2)
English = calcPoint(grade3)
history = calcPoint(grade4)
spanish = calcPoint(grade5)
computer = calcPoint(grade6)
government = calcPoint(grade7)

GPA = (math + science + English + history + spanish + computer + government)/7


print("Your GPA is",GPA)
