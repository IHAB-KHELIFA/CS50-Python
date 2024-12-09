def camel_to_snake(camel_case):
    snake_case = ""  # Initialize an empty string for the snake_case result
    for char in camel_case:
        if char.isupper():  # Check if the character is uppercase
            snake_case += "_" + char.lower()  # Add an underscore and convert to lowercase
        else:
            snake_case += char  # Add the character as is if it's not uppercase
    return snake_case

# Prompt the user for input
camel_case_input = input("Enter a camelCase variable name: ")

# Convert to snake_case
snake_case_output = camel_to_snake(camel_case_input)

# Output the result
print("Snake case variable:", snake_case_output)
