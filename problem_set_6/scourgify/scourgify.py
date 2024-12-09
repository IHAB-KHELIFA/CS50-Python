import sys
import csv
import os

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input.csv output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # Read the input CSV file
        with open(input_file, newline='') as file:
            reader = csv.DictReader(file)

            # Prepare to write to the output CSV file
            with open(output_file, 'w', newline='') as new_file:
                # Specify fieldnames for the output CSV
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()  # Write header row

                # Process each row in the input file
                for row in reader:
                    # Split the name field into last and first names
                    last, first = row['name'].split(", ")
                    house = row['house']

                    # Write the reformatted row to the output file
                    writer.writerow({
                        'first': first,
                        'last': last,
                        'house': house
                    })

    except FileNotFoundError:
        print(f"Error: Could not read '{input_file}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
