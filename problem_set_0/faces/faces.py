# Main function to prompt the user for input and print the converted result
def main():
    # Get input from the user
    user_input = input("Please enter a string: ")

    # Call the convert function on the user's input and print the result
    print(convert(user_input))

# Function to convert :) and :( to their emoji equivalents
def convert(input_str):
    input_str = input_str.replace(":)", "\U0001F642").replace(":(", "\U0001F641")
    return input_str



# Call the main function at the bottom of the file
if __name__ == "__main__":
    main()
