# shopping_list_manager.py

def display_menu():
    """Displays the menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Manages adding, removing, and viewing items in the shopping list.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True: # Loop continuously until the user chooses to exit
        display_menu() # Show the menu
        choice = input("Enter your choice: ").strip() # Get user's choice and clean it up

        if choice == '1':
            # Add an item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the input is not empty
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to your list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove an item
            if not shopping_list: # Check if the list is empty first
                print("Your shopping list is empty. Nothing to remove.")
                continue # Skip to the next loop iteration
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove: # Ensure the input is not empty
                if item_to_remove in shopping_list: # Check if the item exists in the list
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from your list.")
                else:
                    print(f"'{item_to_remove}' not found in the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to get numbered list
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit the program
            print("Goodbye! Happy shopping!")
            break # Exit the while loop
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()