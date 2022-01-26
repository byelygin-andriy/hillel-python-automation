# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# Программа получает на вход числа n и m.

km_per_day = float(input("Input distance per day in kilometers: "))
distance_to_destination = float(input("Input distance to destination in kilometers: "))

if km_per_day <= 0 or distance_to_destination <= 0:
    print("Distance cannot be negative or 0")
else:
    time_to_destination = distance_to_destination / km_per_day
    days_to_destination = int(time_to_destination // 1)
    hours_in_day = 24
    hours_to_destination = int((time_to_destination % 1) * hours_in_day)
    print(f"{days_to_destination} days and {hours_to_destination} hours needed to reach the destination")
