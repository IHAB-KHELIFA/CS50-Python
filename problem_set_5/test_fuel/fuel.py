def main():
    fraction = input("Enter fuel level (X/Y): ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        print("Invalid input")

def convert(fraction):
    try:
        # Split fraction into X and Y
        x, y = map(int, fraction.split('/'))

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator")

        # Calculate the fraction as a percentage
        percentage = round((x / y) * 100)
        return max(0, min(percentage, 100))  # Clamp value between 0 and 100
    except (ValueError, ZeroDivisionError) as e:
        raise e  # Re-raise exceptions for handling in main

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
