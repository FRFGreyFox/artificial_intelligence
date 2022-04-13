'''a = [1, 2, 3, 4, 5]
b = list('итерируемый объект')
c = [i for i in range(5)]
print('можно_так:', a)
print('можно_так_2:', b)
print('а_можно_и_так:', c)
print('можно_так[0]:', a[4])
print('можно_так[0]:', b[0])
print('а_можно_и_так[3]:', c[2])

example_array = [[-1, 0, 0, 1], [2, 3, 5, 8]]
print(example_array[0])
print(example_array[1])
print(example_array[1][2])'''

n = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(n):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)
