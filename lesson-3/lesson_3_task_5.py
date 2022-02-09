# Напишите программу, которая удаляет дубликаты элементов из списка.

original_list = [1, 1, 2, 3, 3, 4, 5, 5, 7, 1, 9, 8, 9]

temp_list = []

for i in original_list:
    if i not in temp_list:
        temp_list.append(i)

print(temp_list)
