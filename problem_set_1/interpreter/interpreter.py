def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an expression (x y z): ")

    # Split the input into components
    x_str, operator, z_str = expression.split()

    # Convert x and z to integers
    x = int(x_str)
    z = int(z_str)

    # Perform the calculation based on the operator
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        raise ValueError("Invalid operator")

    # Print the result formatted to one decimal place
    print(f"{result:.1f}")


# Run the program
main()
