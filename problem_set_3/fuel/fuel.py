def get_fuel_percentage():
    while True:
        try:
            # Prompt the user for a fraction
            fraction = input("Fraction: ")

            # Split the input on '/'
            x, y = fraction.split("/")

            # Convert x and y to integers
            x = int(x)
            y = int(y)

            # Check if Y is zero
            if y == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")

            # Check if X is greater than Y
            if x > y:
                raise ValueError("Numerator cannot be greater than denominator.")

            # Calculate the percentage
            percentage = round((x / y) * 100)

            # Return the appropriate output based on the percentage
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except ValueError:
            # Handle cases where input is not valid integers or fraction is invalid
            print("Invalid input. Please enter a valid fraction.")
        except ZeroDivisionError:
            # Handle division by zero specifically
            print("Invalid input. Denominator cannot be zero.")

# Main function to display the result
if __name__ == "__main__":
    print(get_fuel_percentage())
