import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial requires a non-negative integer"
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def parse_number(value):
    if "j" in value or "J" in value:
        return complex(value)
    if "." in value:
        return float(value)
    return int(value)

def main():
    op = input("Enter operation (+, -, *, /, %, factorial): ").strip()

    if op == "factorial":
        value = input("Enter integer: ").strip()
        try:
            n = parse_number(value)
            print("Result:", factorial(n))
        except Exception as e:
            print("Error:", e)
        return

    a = input("Enter first value: ").strip()
    b = input("Enter second value: ").strip()
    try:
        a_val = parse_number(a)
        b_val = parse_number(b)
    except Exception as e:
        print("Error:", e)
        return

    if op == "+":
        result = add(a_val, b_val)
    elif op == "-":
        result = subtract(a_val, b_val)
    elif op == "*":
        result = multiply(a_val, b_val)
    elif op == "/":
        result = divide(a_val, b_val)
    elif op == "%":
        result = modulus(a_val, b_val)
    else:
        print("Error: invalid operation")
        return

    # Round floats to 2 decimal places for display
    if isinstance(result, float):
        result = round(result, 2)

    print("Result:", result)

if __name__ == "__main__":
    main()