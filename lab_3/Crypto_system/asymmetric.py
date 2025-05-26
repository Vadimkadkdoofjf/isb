from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from typing import Tuple

from filework import FileWork

class AsymmetricEncryption:
    """
    RSA
    """
    def __init__(self):
        self.pb_key = None
        self.pr_key = None

    def generate_asymmetric_keys(self) -> Tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generates public and private keys
        :return: tuple of public and private keys
        """
        keys = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = 2048
        )
        self.pr_key = keys
        self.pb_key = keys.public_key()
        return self.pb_key, self.pr_key

    def serialization_public_key(self, path_to_save: str) -> None:
        """
        Serializes public key
        :param path_to_save: Path to save the public key
        :return: None
        """
        FileWork.write_public_key(path_to_save, self.pb_key)

    def serialization_private_key(self, path_to_save: str) -> None:
        """
        Serializes private
        :param path_to_save: Path to save the public key
        :return: None
        """
        FileWork.write_private_key(path_to_save, self.pr_key)

    @staticmethod
    def deserialization_public_key(file: str) -> rsa.RSAPublicKey:
        """
        Deserializes public key
        :param file: path to the public key
        :return: RSA public key
        """
        return FileWork.read_pb_key(file)

    @staticmethod
    def deserialization_private_key(file: str) -> rsa.RSAPrivateKey:
        """
        Deserializes private key
        :param file: Path to the file with private key
        :return: RSA private key
        """
        return FileWork.read_pr_key(file)

    def encrypt_symmetric_key(self, path_to_public: str, symmetric_key: bytes, path_to_save: str) -> bytes:
        """
        Encrypts key
        :param path_to_public: path to the RSA public key
        :param symmetric_key: symmetric key
        :param path_to_save: path to save key
        :return: None
        """
        public_key = self.deserialization_public_key(path_to_public)
        text = public_key.encrypt(symmetric_key, padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(), label=None
            )
        )
        FileWork.write_bytes(path_to_save, text)
        return text

    def decrypt_symmetric_key(self, path_to_private: str, path_encrypted: str) -> bytes:
        """
        Decrypts symmetric key
        :param path_to_private: path to the RSA private key
        :param path_encrypted: path to the encrypted key
        :return: None
        """
        pr_key = self.deserialization_private_key(path_to_private)
        encrypted_sym_key = FileWork.get_bytes(path_encrypted)
        dc_text = pr_key.decrypt(encrypted_sym_key,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(), label=None))

        return dc_text
