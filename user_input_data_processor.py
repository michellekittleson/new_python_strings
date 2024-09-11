# Task 1: Input Length Validator

def length_validator():
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")

    if len(user_first_name) >= 2 and len(user_last_name) >= 2:
        print("Valid first and last name")
    else:
        print("Make sure both first and last names are at least 2 characters long.")

length_validator()