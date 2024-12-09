def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    # Convert to lowercase for case-insensitive comparison
    greeting = greeting.lower().strip()

    # Check conditions and return appropriate value
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
