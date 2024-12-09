def grocery_list():
    dict = {}
    while True:
        try:
            item = input().lower()
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1


        except EOFError:
            break
    sorted_list = sorted(dict.items())
    for item, count in sorted_list:
        print(f"{count} {item.upper()}")

  # Main function
if __name__ == "__main__":
    grocery_list()

