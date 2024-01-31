import re

def password_strength(password):
    """Check the strength of a password."""
    if len(password) <8:
        return "password is to short. It should be at least 8 characters."
    
    strength_checks = [
        [r'[a-z]', "lowercase letter"],
        [r'[A-Z]', "uppercase letter"],
        [r'[0-9]',"number"],
        [r'[^a-zA-Z0-9]',"symbol"]
        ]
    missing_elements = []

    for check, element in strength_checks:
        if not re.search(check, password):
            missing_elements.append(element)
          
    if missing_elements:
      return f"password should contain at least one {', '.join(missing_elements)}."

    return "password is strong."
            
def main():
                password = input("Enter a password to check its strength: ")
                result = password_strength(password)
                print(result)

if __name__ == "__main__":
    main()


