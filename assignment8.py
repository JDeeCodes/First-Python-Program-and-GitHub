"""Programming Assignment 8: Manage sample credentials with a dictionary."""

# Part 1: Working with a dictionary
# Assignment 7 used a tuple and a set. Here, each username is a dictionary
# key, and its sample password is the corresponding value.
credentials = {}

print("Credentials Manager")
print("Use sample usernames and passwords to test the program.")

# Part 2: The user can add, remove, display, and search for credentials.
while True:
    print("\n1. Add 2. Remove 3. Display 4. Search 5. Exit")
    choice = input("Choose an option (1-5): ").strip() 

    if choice == "1":
        username = input("Enter a username: ").strip()
        password = input("Sample password: ")

        if not username or not password.strip():
            print("Username and password are required.")
        elif username in credentials:
            print("that username already exists. Use a different username.") 
        else:
            # Like colors.add(), this entry, now as a key-value pair
            credentials[username] = password
            print(f"Added {username}.")

    elif choice == "2":
        username = input("Enter the username to remove: ").strip() 
        # Replace colors.remove() with deletion by username (the key) from the dictionary.
        if username in credentials:
            del credentials[username]
            print(f"Removed {username}.")
        else:
            print(f"{username} not found.")

    elif choice == "3":
        if credentials:
            print("Saved Credentials:") 
            # like color loop, visit each entry. items() gives both the key and value for each entry in the dictionary.
            for username, password in credentials.items():
                print(f"{username}: {password}")
        else:
            print("No credentials stored.")
    elif choice == "4":
        username = input("Enter the username to search for: ").strip() 
        # Like "Monday" in days, check membership before reading the value. 
        if username in credentials:
            print(f"Password for {username}: {credentials[username]}")
        else:
            print(f"Username {username} not found.")
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 5.")