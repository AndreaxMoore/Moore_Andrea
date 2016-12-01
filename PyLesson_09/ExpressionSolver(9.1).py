expression = input("Please enter a mathematical expression: ")
equation = expression.split(" ")

i = 0
while i < len(equation):
    if i < len(equation) and equation[i]== ("*" or "/"):
        if equation[i] == "*":
            equation.append(equation[i-1]*(i+1))
        else:
            equation.append(equation[i-1]/(i+1))
        equation.remove(equation[i-1])
        equation.remove(equation[i])
    i += 1


    if i < len(equation) and equation[i] == ("+" or "-"):
        if equation[i] == "+":
            equation.append(equation[i-1]+(i+1))
        else:
            equation.append(equation[i-1]-(i+1))
        equation.remove(equation[i-1])
        equation.remove(equation[i])
    i += 1
print(equation)
        
        
    
