def coke_machine():
    # Total cost of the Coke bottle
    cost = 50
    # Amount due initially
    amount_due = cost

    # List of accepted coin denominations
    accepted_coins = [25, 10, 5]

    # Keep asking for coins until the amount due is paid
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")

        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the coin is in the accepted denominations
        if coin in accepted_coins:
            amount_due -= coin  # Reduce the amount due by the inserted coin

    # If the amount_due is negative, calculate the change
    change = abs(amount_due)  # abs() ensures the change is positive

    # Output the change, if any
    print(f"Change Owed: {change}")

# Run the coke machine function
coke_machine()
