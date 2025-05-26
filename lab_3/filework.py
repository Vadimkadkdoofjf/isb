import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
class FileWork:

    @staticmethod
    def get_bytes(file: str) -> bytes:
        """
        Reads data from the file
        :param file: Path to the file
        :return: Bytes format object
        """
        try:
            with open(file, 'rb') as f:
                data = f.read()
            return data
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise  FileNotFoundError(f"The file was not found.")

    @staticmethod
    def write_bytes(path_to_save: str, data: bytes) -> None:
        """
        Writes data to the file
        :param path_to_save: Path to save the file
        :param data: data to save
        :return:
        """
        try:
            with open(path_to_save, mode='wb') as f:
                f.write(data)
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise  FileNotFoundError(f"The file was not found.")

    @staticmethod
    def write_text(path_to_save: str, text: str) -> None:
        """
        Writes text to file
        :param path_to_save: path to save the file
        :param text: Text to save
        :return:
        """
        try:
            with open(path_to_save, 'w') as f:
                f.write(text)
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")

    @staticmethod
    def read_text(file: str) -> str:
        """
        Reads text from the file
        :param file: Path to the file
        :return: Text from the file
        """
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")

    @staticmethod
    def write_json(path_to_save: str, data: dict) -> None:
        """
        Saves data to json
        :param path_to_save: path to save the json
        :param data: Data to save
        :return: None
        """
        try:
            with open(path_to_save, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")

    @staticmethod
    def read_json(file: str) -> dict[str, str]:
        """
        Reads json from the file
        :param file: Path to the file
        :return: Dict of [str, str]
        """
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")

    @staticmethod
    def write_public_key(path_to_save: str, public_key: rsa.RSAPublicKey) -> None:
        """
        Serializes public key to the file
        :param path_to_save: path to save the public key
        :param public_key: RSA public key
        :return: None
        """
        try:
            with open(path_to_save, 'wb') as out:
                out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise  FileNotFoundError(f"The file was not found.")

    @staticmethod
    def write_private_key(path_to_save: str, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serializes private key to the file
        :param path_to_save: path to save the private key
        :param private_key: RSA private key
        :return:
        """
        try:
            with open(path_to_save, 'wb') as out:
                out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                            encryption_algorithm=serialization.NoEncryption()))
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")

    @staticmethod
    def read_pb_key(file: str) -> rsa.RSAPublicKey:
        """
        Deserializes public key from the file
        :param file: path to the file
        :return: RSA public key
        """
        try:
            with open(file, 'rb') as pem_in:
                public_bytes = pem_in.read()
                return load_pem_public_key(public_bytes)
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")

    @staticmethod
    def read_pr_key(file: str) -> rsa.RSAPrivateKey:
        """
        Deserializes private key from the file
        :param file: Path to the file
        :return: RSA private key object
        """
        try:
            with open(file, 'rb') as pem_in:
                private_bytes = pem_in.read()
                return load_pem_private_key(
                    private_bytes, password=None)
        except Exception as e:
            raise Exception(f"An error occurred with the file: {str(e)}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file was not found.")