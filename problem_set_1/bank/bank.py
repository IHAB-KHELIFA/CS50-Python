def main():
    greeting = input("Greeting: ").strip().lower()
    print(determine_value(greeting))


def determine_value(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


main()
