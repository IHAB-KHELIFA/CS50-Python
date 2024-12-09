import emoji

def main():
    # Prompt user for input
    text = input("Input: ")

    # Convert any emoji codes or aliases in the text to emojis
    emojized_text = emoji.emojize(text,language='alias')

    # Output the emojized text
    print("Output:", emojized_text)

if __name__ == "__main__":
    main()
