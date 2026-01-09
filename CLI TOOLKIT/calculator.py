# calculator.py

def add(a, b):
    return a + b

def expo(a,b):
    return a ** b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculator():
    while True:
        try:
            op = input("\nCalculator (+ ,-, *,**, /, back): ")
            if op == "back":
                return

            a = float(input("First number: "))
            b = float(input("Second number: "))

            if op == "+":
                print("Result:", add(a, b))
            elif op == "-":
                print("Result:", sub(a, b))
            elif op == "*":
                print("Result:", multiply(a, b))
            elif op == "**":
                print("Result:", expo(a, b))
            elif op == "/":
                print("Result:", divide(a, b))
            else:
                print("Invalid operation")

        except ValueError:
            print("Please enter valid numbers")
