import re
import time

def password_strength(password):
    """Assess the strength of a password based on length and character set.

    Returns a string indicating the password's strength:
    - 'Very weak' (length < 8)
    - 'Weak' (length >= 8, but no uppercase or lowercase letters or digits)
    - 'Moderate' (length >= 8 and at least one of uppercase, lowercase letters or digits)
    - 'Strong' (length >= 12 and at least one of each uppercase, lowercase letters, digits, and special characters)
    - 'Very strong' (length >= 16 and at least one of each uppercase, lowercase letters, digits, and special characters)
    """

    # Check length
    if len(password) < 8:
        return 'Very weak'
    elif len(password) < 12:
        strength = 'Weak'
    elif len(password) < 16:
        strength = 'Moderate'
    else:
        strength = 'Strong'

    # Check for presence of uppercase and lowercase letters, digits, and special characters
    if (
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    ):
        strength = 'Very strong'
    elif (
        re.search(r'[A-Z]', password) or
        re.search(r'[a-z]', password) or
        re.search(r'\d', password) or
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    ):
        strength = 'Moderate'

    return strength

def main():
    print("-----------------------------------------------")
    print("            Password Strength Checker          ")
    print("-----------------------------------------------")

    while True:
        password = input("Enter the password (or type 'quit' to exit): ")
        print("                                ")

        if password.lower() == 'quit':
            break

        # Add a delay of 1 second
        time.sleep(0.5)

        pw_strength = password_strength(password)
        print(f" {password} is: {pw_strength.capitalize()}\n")

if __name__ == "__main__":
    main()