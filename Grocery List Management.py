def display_menu():
    print("\n===== Grocery List Manager =====")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display grocery list")
    print("4. Show total items")
    print("5. Exit")

# Using list to store grocery items
grocery_list = []

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter item to add: ")
        grocery_list.append(item)
        print(f"'{item}' has been added to your grocery list.")

    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"'{item}' has been removed from your grocery list.")
        else:
            print(f"'{item}' is not in your grocery list.")

    elif choice == '3':
        if grocery_list:
            print("\nYour Grocery List:")
            for index, item in enumerate(grocery_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Your grocery list is empty.")

    elif choice == '4':
        print(f"Total items in your grocery list: {len(grocery_list)}")

    elif choice == '5':
        print("Exiting Grocery List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
