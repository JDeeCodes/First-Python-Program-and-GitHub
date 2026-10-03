# Part 1: Positive, Negative, or Zero
number = input("Enter a number: ")
number = int(number)

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Part 2: Age Check
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("You are 18 or older.")
else:
    print("You are under 18.")


# Part 3: Number Selection
choice = input("Enter a number from 1 to 3: ")
choice = int(choice)

if choice == 1:
    print("You selected number 1.")
elif choice == 2:
    print("You selected number 2.")
elif choice == 3:
    print("You selected number 3.")
else:
    print("Invalid selection.")
    print("You selected number 3.")
else:
    print("Invalid selection.")
