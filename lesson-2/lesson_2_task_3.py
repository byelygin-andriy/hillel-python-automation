# Найти максимальное число из трех. Числа вводится с клавиатуры

first_number = int(input('Input first number: '))
second_number = int(input('Input second number: '))
third_number = int(input('Input third number: '))
if first_number > second_number and first_number > third_number:
    print(f"The biggest number is {first_number}")
elif second_number > first_number and second_number > third_number:
    print(f"The biggest number is {second_number}")
elif third_number > first_number and third_number > second_number:
    print(f"The biggest number is {third_number}")
else:
    print("The numbers are equal")
