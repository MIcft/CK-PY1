# Дан целочисленный список, состоящий из 10 элементов.
# Поменять местами первый максимальный и последний элементы.

list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
first_max = max(list_numbers)
index_first_max = list_numbers.index(first_max)
list_numbers[index_first_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_first_max]
print(list_numbers)
