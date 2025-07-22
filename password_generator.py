import random
import string

def generate_password(length):
    # All possible characters
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    while True:
        try:
            length = int(input("Enter desired password length (minimum 6): "))
            if length < 6:
                print("Please enter a length of at least 6.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
