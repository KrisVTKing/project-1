
#favorite_foods = ["apple", "banana", "carrot", "donut", "eggplant", "fish", "grapes", "hamburger", "ice cream", "jelly"]
#add_foods = input("Add a new food to the list: ")
#remove_foods = input("Remove a food from the list: ")
#favorite_foods.append(add_foods)
#favorite_foods.remove(remove_foods)
#print(favorite_foods)
favorite_foods = ["apple", "banana", "carrot", "donut", "eggplant", "fish", "grapes", "hamburger", "ice cream", "jelly"]
def add_food():
    while True:
        add_foods = input("Add a new food to the list: ")
        confirm = input("Are you sure you want to add \033[1;32m" + add_foods + "\033[0m to the list? (Yes/No) ")
        if confirm.lower() == "yes":
            favorite_foods.append(add_foods)
            print(f"{add_foods} has been added to the list.")
            break
        elif confirm.lower() == "no":
            print("No item is added to the list.")
            break
        else:
            print("Invalid input. No item is added to the list.")

def remove_food():
    while True:
        remove_foods = input("A food to remove from the list: ")
        if remove_foods in favorite_foods:
            confirm = input("Are you sure you want to remove \033[32m" + remove_foods + "\033[0m from the list? (Yes/No) ")
            if confirm.lower() == "yes":
                favorite_foods.remove(remove_foods)
                print(f"{remove_foods} was removed from the list.")
                break
            elif confirm.lower() == "no":
                print("No item was removed from the list.")
                break
            else:
                print("Invalid input. No item was removed from the list.")
        else:
            print("Food not found in the list.")

while True:
    main_menu = input("Please select an option: View, Add, Remove or Exit: ").lower()
    if main_menu == "view":
        print(favorite_foods)
    elif main_menu == "add":
        add_food()
    elif main_menu == "remove":
        remove_food()
    elif main_menu == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid input.")