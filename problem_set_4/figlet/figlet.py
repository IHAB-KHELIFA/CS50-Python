import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Specific font requested, check if it's valid
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Error: Invalid font name.")
    else:
        # Invalid usage
        sys.exit("Usage: figlet.py [-f FONT_NAME]")

    # Set the font
    figlet.setFont(font=font)

    # Prompt the user for text input
    text = input("Input: ")

    # Output the text in the specified or random font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
