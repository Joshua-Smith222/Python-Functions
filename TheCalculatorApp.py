#task 1
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error division by zero"
    else:
        return x / y

#task 2
def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Divide")
    choice = input("enter choice (1/2/3/4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input, please select a valid operation.")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please select valid numbers.")
        return
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if result == "Error division by zero":
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")
#task 3
calculator()
