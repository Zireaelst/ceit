first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter the operation (+, -, *, /):")


def addition():
    return first_number + second_number

def subtraction():
    return first_number - second_number

def multiplication():
    return first_number * second_number

def division():
    if second_number == 0:
        print("can't be division by zero ")
    else:
        return first_number / second_number

def calculation(addition, subtraction, multiplication, division):
    if operation == "addition" or operation == "+":
        return addition()
    elif operation == "subtraction" or operation == "-":
        return subtraction()
    elif operation == "multiplication" or operation == "*":
        return multiplication()
    elif operation == "division" or operation == "/":
        return division()

print(calculation(addition, subtraction, multiplication, division))



