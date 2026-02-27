# calculator.py

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Choose operation (+, -, *, /): ")

        result = calculate(num1, num2, operator)
        print("Result:", result)

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()