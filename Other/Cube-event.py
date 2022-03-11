import random

event1_2 = 'Ваш герой погиб'
event3_4 = 'Ваш герой улучшен'
event5_6 = 'Ваш герой победил'

a = range(1, 7)

dice_roll = random.choice(range(1, 7))

print('Результат бросания кубиков', dice_roll)

if dice_roll <= 2:
    print(event1_2)
elif dice_roll <= 4:
    print(event3_4)
elif dice_roll <= 5:
    print(event5_6)
else:
    print('Вышла ошибка')
