def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length (must be between 2 and 6 characters)
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for allowed characters and number placement rules
    found_number = False
    for i, char in enumerate(s):
        # Only alphanumeric characters allowed
        if not char.isalnum():
            return False

        # Once we find a number, all following characters must be numbers
        if char.isdigit():
            # First number can't be '0'
            if not found_number and char == '0':
                return False
            found_number = True
        elif found_number and char.isalpha():
            # No letters allowed after numbers
            return False

    return True


if __name__ == "__main__":
    main()
