#
# Написать функцию, которая возвращает список, заполненный случайными целыми числами. Числа в списке должны быть уникальными.
# Диапазон случайных чисел от -10 до 10 включительно. Размер списка 15 чисе
# TODO написать функцию для получения списка уникальных целых чисел
from random import randint

def get_unique_list_numbers() -> list[int]:
    list_= [randint(-10, 10) for i in range(15)]
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
