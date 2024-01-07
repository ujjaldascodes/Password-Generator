import random
import string

def generate_password(length=6, letters_count=2, numbers_count=2, symbols_count=2):
    if length < letters_count + numbers_count + symbols_count:
        raise ValueError("Total length is less than the sum of letters, numbers, and symbols count.")

    letters = random.choices(string.ascii_letters, k=letters_count)
    numbers = random.choices(string.digits, k=numbers_count)
    symbols = random.choices(string.punctuation, k=symbols_count)

    password_list = letters + numbers + symbols

    # Ensuring the total length matches the specified length
    while len(password_list) < length:
        password_list.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    random.shuffle(password_list)

    return ''.join(password_list)

# Test cases
print(generate_password(length=8, letters_count=3, numbers_count=3, symbols_count=2))
print(generate_password())
print(generate_password(length=10, letters_count=4, numbers_count=3, symbols_count=3))
