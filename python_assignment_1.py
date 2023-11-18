print("This is Assignment1")

import re

def check_password_strength(password):
    special_char = r"[!@#$%^&*(),.?\":{}|<>]"

    if len(password) < 8:
        return False
    if not any(i.isupper() for i in password) or not any(i.islower() for i in password):
        return False
    if not any(i.isdigit() for i in password):
        return False
    if not re.search(special_char, password):
        return False
    return True

def main():
    password = input("Enter your password: ")

    output = check_password_strength(password)

    if output:
        print("Password is strong")
    else:
        print("password is weak")

if __name__=="__main__":
    main()