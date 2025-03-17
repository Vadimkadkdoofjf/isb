
import json
from file import open_file, save
from task_1.Caesar_Code import caesar_code
from task_2.frequency_analysis import calculate_frequencies, create_key, decode_text

def task_1():
    task1_files = open_file("settings.json").get("task_1")
    text = open_file(task1_files["input_file"])
    key = open_file(task1_files["key"])
    shift = key.get('shift')

    if not isinstance(shift, int):
        raise ValueError("Значение shift должно быть целым числом.")

    encrypted_text = caesar_code(text, shift)
    save(task1_files["output_file"], encrypted_text)

def task_2():
    task2_files = open_file("settings2.json").get("task_2")
    text = open_file(task2_files["input_file"])
    russian_freq = open_file(task2_files["russian_freq"])
    my_freq = calculate_frequencies(text)
    save(task2_files["freq"],my_freq)
    key = create_key(russian_freq,my_freq)
    save(task2_files["key"],key)
    final_text = decode_text(text,key)
    save(task2_files["output_file"],final_text)

def main():
    task_1()
    task_2()

if __name__ == "__main__":
    main()


