def calculate_pow(x, n):
    return x ** n

def calculate_add(x, n):
    return x + n

def calculate_sub(x, n):
    return x - n

def calculate_mul(x, n):
    return x * n

def calculate_div(x, n):
    if n != 0:
        return x / n
    else:
        return "Cannot divide by zero"
x = float(input("Enter the value of x: "))
n = float(input("Enter the value of n: "))
operation = input("Choose operation (pow, add, sub, mul, div): ")
if operation == "pow":
    result = calculate_pow(x, n)
elif operation == "add":
    result = calculate_add(x, n)
elif operation == "sub":
    result = calculate_sub(x, n)
elif operation == "mul":
    result = calculate_mul(x, n)
elif operation == "div":
    result = calculate_div(x, n)
else:
    result = "Invalid operation"

print(f"Result of {operation}({x}, {n}): {result}")
