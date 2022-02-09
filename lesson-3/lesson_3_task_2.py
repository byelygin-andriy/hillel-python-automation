# Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.

number = int(input("input a number that bigger than 1 to print an triangle: "))
star = str("*")
if number > 1:
    for i in range(0, number, 1):
        print(star*i)
    for i in range(number, 0, -1):
        print(star*i)
else:
    print("number should be bigger than 1")
