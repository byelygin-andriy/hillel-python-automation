# Напишите программу, которая выводит словарь, в котором ключи представляют собой числа от 1 до 15 (оба включены),
# а значения представляют собой квадраты ключей. Генерация ключей и значений должна быть выполнена через цикл.

dicts = {}
first_key = 1
last_key = 15

for key in range(first_key, last_key + 1):
    value = key ** 2
    dicts[key] = value

print(dicts)
