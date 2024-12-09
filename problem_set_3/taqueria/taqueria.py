def Menu():
    total_cost = float(0)
    while True:
        menu = {
                "baja taco": 4.25,
                "burrito": 7.50,
                "bowl": 8.50,
                "nachos": 11.00,
                "quesadilla": 8.50,
                "super burrito": 8.50,
                "super quesadilla": 9.50,
                "taco": 3.00,
                "tortilla salad": 8.00
            }
        try:
            # Prompt user for an item (case insensitive)
            item = input("Item: ").lower()

            # Check if the item is in the menu
            if item in menu:
                # Add the item's price to the total cost
                total_cost += menu[item]
                # Display the current total cost, formatted to two decimal places
                print(f"Total: ${total_cost:.2f}")
            else:
                # Ignore items not on the menu
                continue
        except EOFError:
             break


# Main function
if __name__ == "__main__":
    Menu()



