import sys
import os

def count_lines_of_code(filename):
    """Counts the lines of code in a Python file, excluding comments and blank lines."""
    loc = 0  # Initialize line of code counter

    try:
        with open(filename, 'r') as file:
            for line in file:
                stripped_line = line.lstrip()  # Remove leading whitespace
                # Skip blank lines or comment lines
                if stripped_line == '' or stripped_line.startswith('#'):
                    continue
                loc += 1  # Count non-blank, non-comment lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    return loc

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python lines.py filename.py")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith('.py'):
        print("Error: The file must have a .py extension.")
        sys.exit(1)

    # Check if the file exists
    if not os.path.isfile(filename):
        print("Error: The file does not exist.")
        sys.exit(1)

    # Calculate and print the number of lines of code
    loc = count_lines_of_code(filename)
    print(loc)

if __name__ == "__main__":
    main()

