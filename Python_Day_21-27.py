
# Build a Calculator
number1 = int(input("What's the first number?: "))
oper = input("+\n-\n*\n/\nPick an operation: ")
number2 = int(input("What's the next number?: "))

def calculation():
    if(oper == '+'):
        output = number1 + number2
        return print(f"{number1} {oper} {number2} = {output}")
    elif(oper == '-'):
        output = number1 - number2
        return print(f"{number1} {oper} {number2} = {output}")
    elif(oper == '*'):
        output = number1 * number2
        return print(f"{number1} {oper} {number2} = {output}")
    elif(oper == '/'):
        output = number1 / number2
        return print(f"{number1} {oper} {number2} = {output}")
    
calculation()