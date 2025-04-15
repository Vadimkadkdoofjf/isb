from file import*
from tests.freq_bit_test import*
from tests.identical_bits_test import*
from tests.longest_run_of_ones_test import*

def main():
    settings = open_file('settings.json')

    sequences = {
        'cpp': open_file(settings['cpp_seq']),
        'java': open_file(settings['java_seq'])
    }

    results = {}
    for name, seq in sequences.items():
        results[name] = {
            'frequency_test': freq_bit_test(seq),
            'identical_bits_test': ident_test(seq),
            'longest_run_test': long_one_test(seq,settings['pi_values'])
        }

    save(settings['result'], results)
    print(f"Тестирование завершено. Результаты сохранены в {settings['result']}")

if __name__ == '__main__':
    main()





