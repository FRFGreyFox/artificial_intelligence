# Сумма трех чисел:
# Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.

a = int(input('Введите 1 число '))
b = int(input('Введите 2 число '))
c = int(input('Введите 3 число '))
s = a + b + c
print(s)

# Площадь прямоугольного треугольника:
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке.

a = int(input('Введите 1 длину катета '))
b = int(input('Введите 2 длину катета '))
print(a * b / 2)

''' ШНУРКИ

Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда,
расстояние между рядами равно a, а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N.
Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх,
по горизонтали и т.д.” (см. рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком,
длина свободного конца шнурка должна быть l. Какова должна быть длина шнурка для этих ботинок?

Программа получает на вход четыре натуральных числа a, b, l и N — именно в таком порядке —
и должна вывести одно число — искомую длину шнурка. '''
