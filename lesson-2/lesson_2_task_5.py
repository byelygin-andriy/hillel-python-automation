# Определить четное или нечетное число. Число вводится с клавиатуры

number = int(input("Input number: "))
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is not even")
