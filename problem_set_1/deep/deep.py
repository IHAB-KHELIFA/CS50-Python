def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    if is_valid_answer(answer):
        print("Yes")
    else:
        print("No")


def is_valid_answer(answer):
    # Check for the valid answers
    return answer == "42" or answer == "forty-two" or answer == "forty two"


main()
