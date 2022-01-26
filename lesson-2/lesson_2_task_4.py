# Определить високосный год или нет.Число вводится с клавиатуры

year = int(input("Please, input year: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"Year {year} is leap")
else:
    print(f"Year {year} is not leap")
