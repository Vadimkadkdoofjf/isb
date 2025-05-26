from Crypto_system.asymmetric import AsymmetricEncryption
from Crypto_system.symmetric import Symmetric

class Hybrid_Crypto_SyStem:
    """
    Class that works with both algorithms.
    """
    def __init__(self, key_length=128):
        self.symmetric = Symmetric()
        self.asymmetric = AsymmetricEncryption()
        self.len = key_length

    def generate_keys(self, path_to_public: str, path_to_private: str, symmetric_path: str) -> None:
        """
        Generates keys
        :param path_to_public: path to save the RSA public key
        :param path_to_private: path to save the RSA private key
        :param symmetric_path: path to save the encrypted symmetric key
        :return:
        """
        self.asymmetric.generate_asymmetric_keys()
        self.asymmetric.serialization_public_key(path_to_public)
        self.asymmetric.serialization_private_key(path_to_private)
        self.symmetric.generate_key(self.len)
        self.symmetric.key = self.asymmetric.encrypt_symmetric_key(path_to_public, self.symmetric.key, symmetric_path)
        self.symmetric.serialization_symmetric_key(symmetric_path)


    def encrypt_text(self, file: str, path_to_private: str, encrypted_path: str, path_to_save: str) -> None:
        """
        Encrypts data
        :param file: path to plain text
        :param path_to_private: path to the private key
        :param encrypted_path: path to the encrypted symmetric key
        :param path_to_save: path to save text
        :return: None
        """
        self.symmetric.key = self.asymmetric.decrypt_symmetric_key(path_to_private, encrypted_path)
        self.symmetric.encrypt_text(file, path_to_save)

    def decrypt_text(self, encrypted_file: str, path_to_private: str, encrypted_key: str, path_to_save: str) -> None:
        """
        Decrypts text
        :param encrypted_file: path to the encrypted text
        :param path_to_private: path to the private key
        :param encrypted_key: path to the encrypted symmetric key
        :param path_to_save: path to save text
        :return: None
        """
        self.symmetric.key = self.asymmetric.decrypt_symmetric_key(path_to_private, encrypted_key)
        self.symmetric.decrypt_text(encrypted_file, path_to_save)
