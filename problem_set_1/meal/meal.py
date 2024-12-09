def main():
    # Prompt the user for a time in 24-hour format
    time_input = input("what time is it ? ")

    # Convert the time to hours as a float
    hours = convert(time_input)

    # Determine and print the appropriate meal time
    if 7.0 <= hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= hours <= 19.0:
        print("Dinner time")


def convert(time_str):
    # Split the input string by the colon
    hours, minutes = map(int, time_str.split(':'))

    # Convert hours and minutes to a float representing hours
    return hours + minutes / 60


# Run the program
if __name__ == "__main__":
    main()
