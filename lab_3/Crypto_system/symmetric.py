import os
from cryptography.hazmat.decrepit.ciphers import algorithms
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from filework import FileWork


class Symmetric:
    """
    CAST5
    """
    def __init__(self):
        self.key = None

    def generate_key(self, key_len: int) -> None:
        """
        Generates random key
        :param key_len: length of key
        :return:
        """
        if not(40 <= key_len <= 128):
            raise ValueError("Uncorrected key length!")
        self.key = os.urandom(key_len // 8)

    def serialization_symmetric_key(self, path_to_save: str) -> None:
        """
        Writes key to the file
        :param path_to_save: path to save the key
        :return: None
        """
        FileWork.write_bytes(path_to_save, self.key)

    def deserialization_symmetric_key(self, file: str) -> bytes:
        """
        Reads key
        :param file: Path to the file with key
        :return: None
        """
        self.key = FileWork.get_bytes(file)
        return FileWork.get_bytes(file)

    def encrypt_text(self, file: str, path_to_save: str) -> None:
        """
        Encrypts text
        :param file: path to file with plain text
        :param path_to_save: path to save result text
        :return: None
        """
        text = FileWork.get_bytes(file)

        padder = padding.PKCS7(64).padder()
        padded_text = padder.update(text) + padder.finalize()

        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        enc_text = encryptor.update(padded_text) + encryptor.finalize()
        enc_text = iv + enc_text

        FileWork.write_bytes(path_to_save, enc_text)


    def decrypt_text(self, encrypted_path: str, path_to_save: str) -> str:
        """
        Decrypts text
        :param encrypted_path: path to the file with encrypted text
        :param path_to_save: path so save file
        :return: decrypted text
        """
        encrypted_text = FileWork.get_bytes(encrypted_path)

        iv = encrypted_text[:8]
        cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(iv))

        encrypted_text = encrypted_text[8:]
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()

        unpadder = padding.PKCS7(64).unpadder()
        unpadder_dc_text = unpadder.update(decrypted_text) + unpadder.finalize()

        FileWork.write_text(path_to_save, unpadder_dc_text.decode('UTF-8'))

        return unpadder_dc_text.decode('UTF-8')