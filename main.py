import random
import AES_enc
import Base64_enc
import sys


def perform_encryption(file, choice):
    if choice == "aes":
        aes_enc = AES_enc.Encryptor()
        aes_enc.encrypt(file)
        with open(file, 'w') as f:
            f.write(aes_enc.enc)
    elif choice == "b64":
        b64_enc = Base64_enc.Encoder()
        b64_enc.encode(file)
        with open(file, 'w') as f:
            f.write(b64_enc.enc)


def base64_encode(file):
    b64_enc = Base64_enc.Encoder()
    b64_enc.encode(file)
    with open(file, 'w') as f:
        f.write(b64_enc.enc)


def main():
    previous = random.choice(("aes", "b64"))
    if len(sys.argv) != 2:
        print("Usage: python main.py <path>")
        exit()

    file = sys.argv[1]

    for _ in range(6):
        if previous == "b64":
            perform_encryption(file, "b64")
            previous = "aes"
        elif previous == "aes":
            perform_encryption(file, "aes")
            previous = "b64"

    with open(file, 'r') as f:
        existing_content = f.read()

    with open(file, 'w') as f:
        new_content = """from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers.algorithms import AES\n"""
        f.write(new_content)

        f.write(existing_content)


if __name__ == "__main__":
    main()
