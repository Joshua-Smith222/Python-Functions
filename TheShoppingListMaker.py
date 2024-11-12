#task 1
def add_item(shopping_list):
    item = input("Enter the item you wish to add to list: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to your list.")

#task 2
def remove_item(shopping_list):
    item = input("Enter the item you wish to remove from list: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your list.")
    else:
        print(f"'{item}' is not in your shopping list.")

#task 3
def print_list(shopping_list):
    if shopping_list:
        print("\nYour shopping list: ")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("Your shopping list is empty.")

def shopping_list_maker():
    shopping_list = []

    while True:
        print("\nWhat would you like to do?")
        print("1. add item")
        print("2. remove item")
        print("3. Print shopping list")
        print("4. quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Good bye! Your session is ended.")
            break
        else:
            print("Invalid input. Please make a valid choice.")
shopping_list_maker()
