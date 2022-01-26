# Найти корни квадратного уравнения и вывести их на экран, если они есть. Если корней нет, то вывести сообщение об этом.
# Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.

print("Lets find square root of a * x ** 2 + b * x + c = 0")
a = float(input("Input value of a: "))
b = float(input("Input value of b: "))
c = float(input("Input value of c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print('There is no square root')
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"x value is {x}")
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f"x1 value is {x1} and x2 value is {x2}")
