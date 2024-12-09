def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if the length is between 2 and 6 characters
    if not (2 <= len(plate) <= 6):
        return False

    # Check if the plate starts with at least two letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # Check for invalid characters (no periods, spaces, or punctuation)
    if not plate.isalnum():  # isalnum checks if all characters are alphanumeric
        return False

    # Check if numbers are only at the end and if they start with '0'
    number_started = False  # Track if a number has started
    for i, char in enumerate(plate):
        if char.isdigit():
            if not number_started:
                # If the first number is '0', it's invalid
                if char == '0':
                    return False
                number_started = True
        elif number_started and char.isalpha():
            # If letters come after a number, it's invalid
            return False

    # If all conditions are met, return True
    return True


main()
