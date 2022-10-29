def get_count_char(main_str):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
chars_dict = {}
DEFAULT_COUNT = 0

for char in chars_dict:
    chars_dict[char] = chars_dict.get(char, DEFAULT_COUNT) + 1

chars_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower().isalpha()

def new_func(chars_dict):
    return chars_dict.get(), ':', chars_dict.values()




