string = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
string = string.lower()

counted_chars = {}
DEFAULT_COUNT = 0

for char in string:
    counted_chars[char] = counted_chars.get(char, DEFAULT_COUNT) + 1

print(counted_chars)







