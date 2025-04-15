import json

def open_file(path):
    """
    Function to open file
    :param path: path to your file
    :return: content
    """
    file_content = None
    try:
        if path.endswith('.json'):
            with open(path, 'r', encoding='utf-8') as file:
                file_content = json.load(file)
        else:
            with open(path, 'r', encoding='utf-8') as file:
                file_content = file.read()
    except FileNotFoundError:
        print(f"Файл '{path}' не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле '{path}'.")
    except PermissionError:
        print(f"Нет прав на чтение файла '{path}'.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    finally:
        return file_content


def save(file, content):
    """
    Saving files

    :param file: name of file to save
    :param content: content of the file
    """
    try:
        if file.endswith('.json'):
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False, indent=4)
        else:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"Данные сохранены в файл: {file}")
    except PermissionError:
        print(f"Нет прав на запись в файл '{file}'.")
    except TypeError as e:
        if file.endswith('.json'):
            print(f"Ошибка сериализации JSON: {e}")
        else:
            print(f"Невозможно записать содержимое: {e}")
    except Exception as e:
        print(f"Произошла ошибка при сохранении файла: {e}")