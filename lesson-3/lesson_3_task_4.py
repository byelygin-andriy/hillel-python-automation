# Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно.

first_number = int(input("input first number: "))
second_number = int(input("input second number: "))

if first_number < second_number:
    for i in range(first_number, second_number + 1, 1):
        print(i)
else:
    print(f"number {first_number} is bigger than {second_number} or they are equal")
