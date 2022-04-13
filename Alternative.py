# For linear algebra
import numpy as np

# входные данные
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# выходные данные
y = np.array([[0, 0, 1, 1]]).T

# сделаем случайные числа более определёнными
np.random.seed(1)

# функция переработка
def nonlin(x,deriv=False):


if(deriv==True):

# прямое распространение
l0 = X
#l1 = nonlin(np.dot(l0, syn0))

