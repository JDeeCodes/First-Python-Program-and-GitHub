# Ask the user to enter three numbers
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
num3 = input("Enter your third number: ")

# Display the values and their original data types
print(f"The value of num1 is {num1}, and it is of the type {type(num1)}.")
print(f"The value of num2 is {num2}, and it is of the type {type(num2)}.")
print(f"The value of num3 is {num3}, and it is of the type {type(num3)}.")

# Convert the input values from strings to floats
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

# Arithmetic expressions 
print(f"The sum of num1 and num2 is {num1 + num2}.")
print(f"The difference of num1 and num2 is {num1 - num2}.")
print(f"The product of num1 and num2 is {num1 * num2}.")
print(f"The quotient of num1 and num2 is {num1 / num2}.")

# Expressions demonstrating order of operations
result = num1 + num2 * num3
result2 = (num1 + num2) * num3

print(f"The result without parentheses is {result}.")
print(f"The result with parentheses is {result2}.")

# Comparison operators
print(f"Is num1 greater than num2? {num1 > num2}")
print(f"Is num2 less than num3? {num2 < num3}")
print(f"Is num3 equal to num1? {num3 == num1}")
