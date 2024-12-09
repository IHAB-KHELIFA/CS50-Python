import validators

def main():
    email = input("Email Address: ")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(email):
    # Use the validators.email function to validate email
    return validators.email(email)

if __name__ == "__main__":
    main()
