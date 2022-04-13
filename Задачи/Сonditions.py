#Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')



#Даны три целых числа. Определите, сколько среди них совпадающих.

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
#Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


#Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
