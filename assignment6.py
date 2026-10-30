# Create a list containing five different fruits.
fruits = ["Apple", "Banana", "Cherry", "Raspberry", "Blueberry"]

# Display the entire list.
print("Original list:", fruits)

# Display the first, third, and last fruits.
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
print("Last fruit:", fruits[-1])

# Ask the user to enter their favorite fruit.
favorite_fruit = input("Enter your favorite fruit: ")

# Add the favorite fruit to the list.
fruits.append(favorite_fruit)

# Display the updated list.
print("Updated list:", fruits)

# Change the second fruit to Mango.
fruits[1] = "Mango"

# Remove one fruit from the list.
fruits.remove("Blueberry")

# Display the total number of fruits.
print("Total number of fruits:", len(fruits))

# Display each fruit on a separate line.
print("Fruits listed individually:")
for fruit in fruits:
    print(fruit)

# Check whether Apple exists in the list.
if "Apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

# Sort the fruits in alphabetical order.
fruits.sort()

# Display the final sorted list.
print("Final sorted list:", fruits)