# Assignment 5: Flow Control and Branching 
# Check if  a number is positive, negative, or zero
number = input("Enter a number: ")
number = int(number)        
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    

# Check if a person is 18 or older
age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You are 18 or older.")
else:
    print("You are not 18 or older.")   
# Let the user select an option from 1 to 3
choice = input("Enter a number from 1 to 3: ")
choice = int(choice)
if choice == 1:
    print("You selected option 1.")
elif choice == 2:
    print("You selected option 2.")
elif choice == 3:
    print("You selected option 3.")
else:
    print("Invalid choice.")    