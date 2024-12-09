def remove_vowels(text):
    vowels = "AEIOUaeiou"  # Define the vowels in both uppercase and lowercase
    result = ""  # Initialize an empty string to store the result without vowels

    # Iterate through each character in the input text
    for char in text:
        if char not in vowels:  # If the character is not a vowel, add it to the result
            result += char

    return result

# Prompt the user for input
input_text = input("Input: ")

# Call the function to remove vowels and print the result
output_text = remove_vowels(input_text)
print("Output: ", output_text)
