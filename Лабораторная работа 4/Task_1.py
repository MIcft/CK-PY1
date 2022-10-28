def get_count_char(str_):
    str_ = str_.lower()
    alphabet_dict = {}

    for letter in str_:
        if letter in alphabet_dict:
            alphabet_dict[letter] += 1
        elif letter.isalpha():
            alphabet_dict[letter] = 1
    return alphabet_dict


def percent_char(dict_):
    count = sum(dict_.values())
    for letter, value in dict_.items():
        dict_[letter] = round(value / count, 3)
    print(dict_)


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_ = get_count_char(main_str)

print(get_count_char(main_str))
print(percent_char(dict_))
