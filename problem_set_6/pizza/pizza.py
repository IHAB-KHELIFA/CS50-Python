
import sys
import os
import csv
from tabulate import tabulate

def read_csv_file(filename):
    """Reads a CSV file and returns a list of rows as dictionaries."""
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]
        return rows
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python pizza.py filename.csv")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the file has a .csv extension
    if not filename.endswith('.csv'):
        print("Error: The file must have a .csv extension.")
        sys.exit(1)

    # Check if the file exists
    if not os.path.isfile(filename):
        print("Error: The file does not exist.")
        sys.exit(1)

    # Read the CSV file and store rows
    rows = read_csv_file(filename)

    # Format the table as ASCII art using tabulate
    table = tabulate(rows, headers="keys", tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
