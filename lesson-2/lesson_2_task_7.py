"""Дана следующая функция y=f(x):
y = 2x – 10, если x > 0
y = 0, если x = 0
y = 2 * |x| – 1, если x < 0
Найти значение функции по x, который вводиться с клавиатуры"""

x = int(input("Enter x value to count y=f(x): "))
if x > 0:
    y = 2*x - 10
    print(f"Y value is {y}")
elif x < 0:
    y = 2 * abs(x) - 1
    print(f"Y value is {y}")
else:
    y = 0
    print(f"Y value is {y}")
