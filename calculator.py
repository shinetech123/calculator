while True:

    print("\nWelcome To My Calculator")

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    op = input("Enter Operator (+, -, *, /): ")

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
           return "Cannot divide by zero"
        return a / b

    if op == "+":
        print(add(a, b))

    elif op == "-":
        print(sub(a, b))

    elif op == "*":
        print(multiply(a, b))

    elif op == "/":
        print(divide(a, b))

    else:
        print("Invalid operator")

    again = input("Do you want to continue? (yes/no): ")

    if again == "no":
        print("Calculator stopped")
        break
