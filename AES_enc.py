import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import random


def aes_encrypt(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv + ciphertext


class Encryptor:
    def __init__(self):
        self.code = ""
        self.enc = ""

    def encrypt(self, file):
        with open(file, 'rb') as f:
            self.code = f.read() + b"\n#a2fed08061c0121a2976f190ac76abda5b3cf7e2"
        weak_pass = random.randint(1000, 9999)
        key = b'100000000000' + str(weak_pass).encode()
        encrypted = aes_encrypt(key, self.code)
        self.enc = f"""from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers.algorithms import AES
def aes_decrypt(key, ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted_plaintext

ciphertext = {encrypted}
for i in range(1000000000000000, 1000000000009999 + 1):
    try:
        plain = aes_decrypt(str(i).encode(), ciphertext)
        if b'a2fed08061c0121a2976f190ac76abda5b3cf7e2' in plain:
            plain = plain.strip(b"#a2fed08061c0121a2976f190ac76abda5b3cf7e2")
            break
    except ValueError:
        pass
exec(plain)"""
