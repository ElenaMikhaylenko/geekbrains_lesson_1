current_result = int(input("Текущий километраж: "))
expected_result = int(input("Ожидаемый результат: "))
days = 1
while current_result < expected_result:
    current_result *= 1.1
    days += 1
    print(f"Результат на {days} день: {current_result:.2f} км.")
print(f"Необходимое число дней: {days}")
