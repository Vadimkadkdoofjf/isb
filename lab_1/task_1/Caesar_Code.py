def caesar_code(text: str, shift: int) -> str:
    """
    Function to code your text
    :param text: plain text
    :param shift: key to code
    :return: coded text
    """
    alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    code_alph = alph[shift:] + alph[:shift]

    table_to_code = str.maketrans(alph, code_alph)

    return text.translate(table_to_code)
