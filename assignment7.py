# Assignment 7: Tuples and Sets in Python

# Part 1: Working with Tuples
days = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)

print("Days of the week:", days)

print("First day:", days[0])
print("Fourth day:", days[3])
print("Last day:", days[-1])

print("Total days:", len(days))

print("\nEach day:")
for day in days:
    print(day)

if "Monday" in days:
    print("Monday is in the tuple.")
else:
    print("Monday is not in the tuple.")

# Tuples are immutable, so their elements cannot be changed.
# Uncommenting the next line causes a TypeError.
# days[0] = "Holiday"


# Part 2: Working with Sets
colors = {"Red", "Blue", "Green", "Yellow"}

print("\nOriginal colors:", colors)

colors.add("Purple")
colors.remove("Yellow")

favorite_color = input("Enter your favorite color: ")
colors.add(favorite_color)

print("\nEach color:")
for color in colors:
    print(color)

print("Total unique colors:", len(colors))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nUnion:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 minus set2):", set1.difference(set2))
