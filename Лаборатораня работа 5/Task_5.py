# Написать функцию для генерации случайных паролей заданной длины n (по умолчанию 8 символов). В качестве алфавита следует использовать:
#
# Буквы верхнего регистра: A - Z
# Буквы нижнего регистра: a - z
# Цифры: 0 - 9
# Для того чтобы сгенерировать случайную выборку, следует использовать функцию sample из модуля random.
# TODO написать функцию генерации случайных паролей
import string
from random import sample


def get_random_password() -> list:
    list_symbol = string.ascii_letters+string.digits
    list_ = sample(list_symbol, 8)

    return list_


print(get_random_password())

