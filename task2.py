sec_new = int(input("Введите время в секундах: "))
hh = sec_new // 3600
sec_new_rem = sec_new % 3600
mm = sec_new_rem // 60
ss = sec_new_rem % 60
print(f"{hh:02} : {mm:02} : {ss:02}")



