import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.decrepit.ciphers.algorithms import TripleDES
from hybrid_crypto_system.assymetric.assymetric_system import Asymmetric
from hybrid_crypto_system.de_sereliazation.de_serealization import DeSerialization


class Symmetric:
    @staticmethod
    def encrypt_data(plain_text, private_bytes, encrypted_symmetric_key):
        private_key = DeSerialization.deserialization(private_bytes, "private")
        symmetric_key = Asymmetric.decrypt_symmetric_key(
            encrypted_symmetric_key, private_key
        )

        padder = padding.ANSIX923(64).padder()
        padded_text = padder.update(plain_text) + padder.finalize()

        iv = os.urandom(8)
        cipher = Cipher(TripleDES(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        return encrypted_text + iv

    @staticmethod
    def decrypt_data(encrypted_data, private_bytes, encrypted_symmetric_key):
        private_key = DeSerialization.deserialization(private_bytes, "private")
        symmetric_key = Asymmetric.decrypt_symmetric_key(
            encrypted_symmetric_key, private_key
        )

        iv = encrypted_data[-8:]
        text = encrypted_data[:-8]
        cipher = Cipher(TripleDES(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_text = decryptor.update(text) + decryptor.finalize()

        unpadder = padding.ANSIX923(64).unpadder()
        decrypted_text = unpadder.update(padded_text) + unpadder.finalize()
        return decrypted_text