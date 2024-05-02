import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits  # строчные и прописные буквы + цифры
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_unique_passwords(N, K):
    passwords = set()
    while len(passwords) < N:
        password = generate_password(K)
        passwords.add(password)
    return passwords

N = int(input("Введите количество паролей: "))
K = int(input("Введите длину каждого пароля: "))

unique_passwords = generate_unique_passwords(N, K)

print(f"{N} уникальных паролей длиной {K} символов:")
for password in unique_passwords:
    print(password)
