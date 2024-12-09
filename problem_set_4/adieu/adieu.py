import sys
import inflect

def main():
    p = inflect.engine()

    # Collect names from user input
    names = []
    print("Enter names (press Ctrl+D to finish):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass  # End of input (Ctrl+D) reached

    # Format the farewell message
    farewell_message = f"Adieu, adieu, to {p.join(names)}"

    # Output the formatted message
    print(farewell_message)

if __name__ == "__main__":
    main()
