
# функция вычисляет квадраты числа
n = 2
def square_n(n):
    return n**2

print(square_n)


distance = 4
time = 2

# Позиционные аргументы (non_keyword)
def get_speed(distance, time):
    return distance / time

# Важен порядок значений
print(get_speed)
print(get_speed(2, 1) == get_speed(1, 2))

# Именованные аргументы(keyword)
def get_speed(distance, time):
    return distance / time

# В случае именованных важно указывать имя параметра, порядок не важен
print(get_speed(distance=1, time=2) == get_speed(time=2, distance=1))

# Комбинация парaметров
def get_speed(distance, time):
    return distance / time

print(get_speed(1, time=2))

# Рекурсия
def factorial(n):
    result = n
    print(n)
    if n > 1:
        result *= factorial(n - 1)
    return result

print(factorial(4))
# Функция высшего порядка
# Функция используется как аргумент
def high_order_function(func, *params):
    print("calling function: %s" % func)
    func(params)

def print_function(text):
    print('text is:')
    for line in text:
        print(line)



# Анонимная функция (лямбда)
# упрощенный вариант функции без имени и использования ключевых слов def
anonim_func = lambda x: x ** 2
square = anonim_func
print(square(5))

#map, filter, reduce, zip