from datetime import date

# "min" возвращает минимальную возможную date time
print('min: ', date.min)

# "max" возвращает максимально возможную date time
print('max: ', date.max)

# "resolution" возвращает еденицу измерения date time
print('resolution: ', date.resolution)

dt = date(year=2022, month=3, day=9)
print(dt, type(dt))
print(f'year - {dt.year}, month - {dt.month}, day - {dt.day}')

print('weekday: ', dt.weekday())
print('iso weekday: ', dt.isoweekday())
print('iso calendar: ', dt.isocalendar())
print('iso format: ', dt.isoformat())
