# Save this file as add_numbers.py

# Step 1: Take input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Step 2: Convert the inputs to floating-point numbers and add them
# Using float() allows the program to handle both integers and decimals
total_sum = float(num1) + float(num2)

# Step 3: Print the result using an f-string
print(f"The sum of {num1} and {num2} is {total_sum}")
