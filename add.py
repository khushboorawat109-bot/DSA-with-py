# Simple Addition Program Using Function

def add_numbers(a, b):
    return a + b

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function call
result = add_numbers(num1, num2)

# Display result
print("The sum is:", result)