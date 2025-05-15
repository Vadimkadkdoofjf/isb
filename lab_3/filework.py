import json

class FileWork:
    @staticmethod
    def open_file(directory: str, mode: str):
        try:
            with open(directory, mode) as file:
                if directory.endswith(".json"):
                    return json.load(file)
                return file.read()
        except Exception as e:
            raise RuntimeError(f"File error: {str(e)}")

    @staticmethod
    def save(directory: str, data: str | dict, mode: str) -> None:
        try:
            with open(directory, mode) as file:
                if directory.endswith(".json"):
                    json.dump(data, file, ensure_ascii=False, indent=4)
                else:
                    file.write(data)
        except Exception as e:
            raise RuntimeError(f"Save error: {str(e)}")