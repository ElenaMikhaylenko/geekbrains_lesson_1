income = int(input("Введите выручку: "))
loss = int(input("Введите издержки: "))
if income > loss:
    print("Прибыль")
    profit = income - loss
    print(f"Рентабельность: {profit / income}")
    person_count = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на сотрудника: {profit / person_count}")
elif income < loss:
    print("Убыток")
else:
    print("Безубыточность")
