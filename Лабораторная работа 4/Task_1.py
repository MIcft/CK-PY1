#
# Напишите функцию, которая будет принимать строку, а возвращать словарь с частотой каждого символа.
#
# Чтобы не считать символы разного регистра два раза, с помощью метода строки lower перевести строку в нижний регистр
#
# С помощью метода строки isalpha проверяем, что символ является буквой.
# Напишите вторую функцию, которая принимает словарь символов.
# Функция должна вернуть новый словарь, где количество каждого элемента заменено на процентное отношение ко всем символам




def get_count_char(str_):
    separate_list = str_.lower().split()
    separate_list.sort()
    list_ = ' '.join(separate_list)
    alphabet_dict = {}
    for letter in list_:
        if letter in alphabet_dict :
            alphabet_dict[letter] += 1
        elif letter.isalpha():
            alphabet_dict[letter] = 1
    return alphabet_dict

def percent_char(dict_):
    # Расчет сколько всего символов
    count = sum(dict_.values())
    for letter, value in dict_.items():
        dict_[letter] = round(value/count, 3)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_ =  get_count_char(main_str)

print(dict_)
print(percent_char(dict_))
