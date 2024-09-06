import useful_tools

def calculate_numbers(a, b, operation):
    c = 0
    if operation == "+":
        c = a+b
    elif operation == "-":
        c = a-b
    elif operation == "*":
        c = a*b
    elif operation == "/":
        c = a/b
    else:
        print("The operation doesnt exist")
    print("the result equal :" , c)


num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operate = input("Select the operation you need to do (+, -, *, /) ")
calculate_numbers(int(num1), int(num2), operate) ## or float()
##dictionaries
"""
hgjgj
"""

'''\
hugugu'''
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversions["Jan"], monthConversions.get("Feb"))


try:
    number = int(input("enter the number:"))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero", err)
except ValueError:
    print("Invalid input")


#open file

employee_file = open("employee.txt", "r")
print(employee_file.readable())
employee_file.close()

print(useful_tools.roll_dice(10))

#lists

stock_list = []
stock_list.append(1)
stock_list.append(2)
stock_list.append(3)
stock_list.append(4)
stock_list.append(5)
stock_list.index(1, 0)


