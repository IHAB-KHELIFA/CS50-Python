import random

def main():
    level = get_positive_integer("Level: ")

    # Generate the target number
    target = random.randint(1, level)

    # Start guessing loop
    while True:
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()
