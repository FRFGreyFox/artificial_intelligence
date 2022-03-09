from datetime import datetime
# Класс datetime представляет из себя комбинацию даты и времени

print('min: ', datetime.min)
print('max: ', datetime.max)
print('resolution: ', datetime.resolution)

datetime_var = datetime(year=2018, month=1, day=1)
print(datetime_var, type(datetime_var))

datetime_var = datetime(year=2018, month=1, day=1, hour=1, second=20, microsecond=100)
print(datetime_var, type(datetime_var))

# "now" текущее значение даты и времени
print('now: ', datetime_var.now())

# "today" текущее значение даты
print('today: ', datetime_var.today())

# "combine" Позволяет соединить дату, время и временнную зону в один объект datetime
print('combine: ', datetime.combine(datetime_var.date(), datetime.max.time()))

# "replace" Позволяет заменить составляющие datetime на новые
print('replace: ', datetime_var.replace(hour=23))

# "strftime" Преобразование даты в строку
print(datetime_var.strftime('%d-%m-%Y %H:%M:%S'), type(datetime_var))

# "strptime" Для преобразования строки определённого формата в переменную datetime
print(datetime.strptime('17-11-2018 02:19:33', '%d-%m-%Y %H:%M:%S'), type(datetime_var))
