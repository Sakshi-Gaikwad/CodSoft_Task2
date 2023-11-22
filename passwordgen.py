import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
while True:
    try:
        password_length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Generate and display the password
password = generate_password(password_length)
print(f"Generated Password: {password}")
