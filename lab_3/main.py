import argparse
import os.path
from Crypto_system.hybrid import Hybrid_Crypto_SyStem
from const import USER_SETTINGS_FILE, ROOT_DIR
from filework import FileWork


def arg_parser() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", type=str, help=""
                                                       "Changes what to do:"
                                                       "generates keys"
                                                       "encrypts ur text"
                                                       "decrypts ur text")
    arguments = parser.parse_args()
    return arguments.mode

def main():
    settings = FileWork.read_json(USER_SETTINGS_FILE)
    for name, path in settings.items():
        path = os.path.join(ROOT_DIR, path)
        settings[name] = path
    mode = arg_parser()
    hybrid = Hybrid_Crypto_SyStem()
    match mode:
        case "generate":
            hybrid.generate_keys(settings["public_key"],
                                 settings["private_key"],
                                 settings["symmetric_key"])
        case "encrypt":
            hybrid.encrypt_text(settings["plain_text"],
                                settings["private_key"],
                                settings["symmetric_key"],
                                settings["encrypted_text"])
        case "decrypt":
            hybrid.decrypt_text(settings["encrypted_text"],
                                settings["private_key"],
                                settings["symmetric_key"],
                                settings["decrypted_text"])


if __name__ == "__main__":
    main()