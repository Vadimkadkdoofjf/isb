import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding

from hybrid_crypto_system.de_sereliazation.de_serealization import DeSerialization


class Asymmetric:
    @staticmethod
    def generate_keys(key_size: int):
        """
        Generation key
        :param key_size: key size
        :return: encrypted_symmetric_key, serialized_private_key, serialized_public_key
        """
        symmetric_key = os.urandom(key_size // 8)

        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()

        s_private_key = DeSerialization.serialization(private_key, "private")
        s_public_key = DeSerialization.serialization(public_key, "public")

        encrypted_symmetric_key = Asymmetric.encrypt_symmetric_key(
            symmetric_key, public_key
        )

        return encrypted_symmetric_key, s_private_key, s_public_key

    @staticmethod
    def encrypt_symmetric_key(symmetric_key, public_key):
        """
        Symmetric key encryption
        :param symmetric_key: the key to encrypt
        :param public_key: public asymmetric key
        :return: encrypted symmetric key
        """
        return public_key.encrypt(
            symmetric_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

    @staticmethod
    def decrypt_symmetric_key(encrypted_symmetric_key, private_key):
        """
        Symmetric key decryption method
        :param encrypted_symmetric_key: the key to decrypt
        :param private_key: private asymmetric key
        :return: decrypted symmetric key
        """
        return private_key.decrypt(
            encrypted_symmetric_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )