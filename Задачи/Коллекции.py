#LIST
#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], …).

a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

#Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи
# метод count.

print(input().count(' ') + 1)