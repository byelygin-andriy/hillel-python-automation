# Пользователь вводит трехзначное число. Найдите сумму его цифр. (используйте %)

number = int(input("Input three-digit number: "))
if len(str(number)) == 3 and (int(number) > 0):
    digit_three = number % 10
    digit_two = number % 100 // 10
    digit_one = number // 100
    sum_of_digits = digit_one + digit_two + digit_three
    print(f"Sum of digits is: {sum_of_digits}")
else:
    print("You entered wrong number")
