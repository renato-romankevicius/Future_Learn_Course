# Python Program to Make a Simple Calculator

def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2

# Creating a function for integer number input
def intin(prmpt):
    while True:
        try:
            num = int(input(prmpt))
            break
        except ValueError:
            print('Please enter a integer number')
    return num
# Options selection and calculation
operation = 0
while True:
    while True:
        print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction, 5-Quit")
        try:
            operation = int(input("Choose operation 1/2/3/4/5: "))
            if 0 < operation < 6:
                break
            else:
                print('Please enter a valid option')
        except ValueError or RuntimeError:
            print('Please enter a valid option')

    if operation == 5:
        break
    else:
        value1 = intin('Please enter first number: ')
        flag = 0
        while flag == 0:
            value2 = intin('Please enter second number: ')
            if operation == 1 and value2 == 0:
                print('Attention! the denominator shall not be zero')
            else:
                flag = 1
#  Execute the chosen operation
    if operation == 1:
        print(value1, "/", value2, "=", divide(value1, value2))
    elif operation == 2:
        print(value1, "*", value2, "=", multiplication(value1, value2))
    elif operation == 3:
        print(value1, "+", value2, "=", addition(value1, value2))
    elif operation == 4:
        print(value1, "-", value2, "=", subtraction(value1, value2))
    else:
        print("Enter correct operation")
