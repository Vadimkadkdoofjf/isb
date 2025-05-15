from cryptography.hazmat.primitives import serialization
from filework import FileWork

class DeSerialization:
    @staticmethod
    def serialization(key, type_k):
        """
        Serialization key
        :param key:
        :param type_k:
        :return:
        """
        match type_k:
            case "public":
                return key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            case "private":
                return key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )

    @staticmethod
    def deserialization(key, type_k):
        """
        Deserialization key
        :param key: the key to deserialize
        :param type_k: type of key - private or public
        :return: None
        """
        match type_k:
            case "public":
                return serialization.load_pem_public_key(key)
            case "private":
                return serialization.load_pem_private_key(key, password=None)

    @staticmethod
    def serialization_data(data_path, data):
        """
        Serializing the data and saving it
        :param data_path: path to save file
        :param data: data
        :return: None
        """
        FileWork.save(data_path, data, "wb")

    @staticmethod
    def deserialization_data(data_path):
        """
        Deserializing the data
        :param data_path: path to serialized file
        :return: data
        """
        return FileWork.open_file(data_path, "rb")