import random

def main():
    level = get_level()
    score = 0

    # Generate and solve 10 problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        # Give the user up to 3 attempts
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            attempts += 1

        # If the user fails after 3 attempts, show the correct answer
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Output the final score
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Please enter a valid level (1, 2, or 3).")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
