# Building a simple phone book dictionary in Python. 
"""Collect names and phone numbers, then look up one entry by name."""

phone_book = {}

print("Phone Book")

# Ask again if the entry count is not a whole number of zero or more.
while True:
    try:
        entry_count = int(input("How many entries would you like to add? "))
        if entry_count >= 0:
            break
    except ValueError:
        pass
    print("Please enter a whole number of zero or more.")

# Store phone numbers as text to keep leading zeros and punctuation.
for entry_number in range(1, entry_count + 1):
    print(f"\nEntry {entry_number}")
    name = input("Name: ").strip()
    while not name:
        name = input("Please enter a name: ").strip()

    phone_number = input("Phone number: ").strip()
    while not phone_number:
        phone_number = input("Please enter a phone number: ").strip()

    # Entering the same name again updates its phone number.
    phone_book[name] = phone_number

# Display each name and its phone number.
print("\nPhone Book Entries")
if phone_book:
    for name, phone_number in phone_book.items():
        print(f"{name}: {phone_number}")
else:
    print("No entries were added.")

# Look up the name using the spelling and capitalization entered above.
search_name = input("\nEnter a name to search for: ").strip()
if search_name in phone_book:
    print(f"{search_name}'s phone number is {phone_book[search_name]}.")
else:
    print(f"No phone number found for {search_name}.")
