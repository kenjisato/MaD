#!/usr/bin/env python
# coding: utf-8

#---- ch02/list-define-x
x = [5, 8, 9, -1]
x


#---- ch02/list-is-not-vector
x + x
3 * x


#---- ch02/list-times-float-error
3.5 * x


#---- ch02/list-not-number
y = [10, 4.3, "Hello", [1, 2, 3]]
y


#---- ch02/list-get-item
x[0]
x[-1]
y[-2]
y[3][1]


#---- ch02/list-len
len(y)


#---- ch02/list-modify
x[0] = 0
x


#---- ch02-list-names
z = x
z[1] = 1000
x


#---- ch02-list-copy
z = x[:]
z[1] = 0
x
z


#---- ch02/list-empty
[]
[1]


#---- ch02/tuple-define
u = (1, 2, 3)
u
u[2]


#---- ch02/tuple-tuple
()
(1,)


#---- ch02/tuple-assign-error/dnr
u[0] = 0


#---- ch02/numpy-import
import numpy as np


#---- ch02/numpy-array-x
x = np.array([1, 2, 3.0])
x


#---- ch02/numpy-shape
x.ndim
x.shape


#---- ch02/numpy-calc
x = np.array([1, 2, 3.])
y = np.array([-1, 1, 4.])
2 * x + 0.5 * y


#---- ch02/numpy-scalor
np.array([1, 2, 3.]) + 10


#---- ch02/numpy-broadcasting
A = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6],
              [0.7, 0.8, 0.9]])
A
x + A


#---- ch02/numpy-addition-error/dnr
np.array([1, 2, 3.]) + np.array([1, 2, 3., 4])


#---- ch02/numpy-multiplication
x * y
x / y


#---- ch02/numpy-ufun
np.log(x)
np.exp(A)


#---- ch02/numpy-reduce
np.sum(x)
np.max(x)


#---- ch02/numpy-reduce-method
x.max()
x.argmax()


#---- ch02/numpy-reduce-axis1
B = np.array([[90,  90],
              [100, 60],
              [80,  90]])
B


#---- ch02/numpy-reduce-axis2
B.mean(axis=0)
B.mean(axis=1)


#---- ch02/numpy-cumsum
np.cumsum(x)
A.cumprod(axis=0)


#---- ch02/numpy-two-vectors
np.dot(x, y)
np.maximum(x, y)
np.minimum(x, y)
np.cov(x, y)


#---- ch02/numpy-create-array
np.ones(2)
np.zeros((2, 3))


#---- ch02/numpy-create-empty
np.empty((2, 3))


#---- ch02/numpy-fix-seed/noinc
np.random.seed(100)


#---- ch02/numpy-random
np.random.random((3, 2, 2))


#---- ch02/numpy-random-normal
np.random.standard_normal((3, 2))


#---- ch02/numpy-create-eye
np.eye(3)


#---- ch02/numpy-create-diag
np.diag([1, -1, 3.])


#---- ch02/numpy-linspace
np.linspace(0, 1, 5)


#---- ch02/numpy-arange
np.arange(5.0, 7.0, 0.2)
np.arange(6)


#---- ch02/numpy-vector-concat
u = np.array([1, 2, 3, 4]).reshape((2, 2))
u
v = np.array([10, 11])
v
np.c_[u, v]
w = v.reshape((1, 2))
np.r_[u, w]


#---- ch02/numpy-vector-to-be-reshaped
a = np.arange(8)
a


#---- ch02/numpy-vector-reshape
a.reshape((2, 4))
a
a.resize((2, 4))
a


#---- ch02/numpy-transpose
a.transpose()
a.T


#---- ch02/numpy-squeeze
b = np.arange(6).reshape((3, 2, 1))
b
b.squeeze()


#---- ch02/matplotlib-import
import matplotlib.pyplot as plt


#---- ch02/matplotlib-exp/plot
x = np.linspace(0, 5, 200)   # Step 1
y = np.exp(x)                # Step 2
plt.plot(x, y)               # Step 3
plt.show()


#---- ch02/matplotlib-random-walk/plot
# Solid line
eps1 = np.r_[0, np.random.standard_normal(100)]
x1 = np.cumsum(eps1)
# Dashed line
eps2 = np.r_[0, np.random.standard_normal(100)]
x2 = np.cumsum(eps2)

plt.plot(x1, 'k-')
plt.plot(x2, 'k--')
plt.show()


#---- ch02/priceindex-problem-laspeyres

price00 = np.array([40, 80])
price01 = np.array([80, 30])
quantity00 = np.array([3, 6])
quantity01 = np.array([5, 7])

# Laspeyres
sum(price01* quantity00) / sum(price00 * quantity00)


#---- ch02/priceindex-problem-paasche
# Paasche
sum(price01 * quantity01) / sum(price00 * quantity01)


#---- ch02/priceindex-problem-matrix
price = np.array([[40, 80],
                  [80, 30]])
price
quantity = np.array([[3, 6],
                     [5, 7]])
quantity


#---- ch02/priceindex-problem-matrix-index
quantity[0, :]


#---- ch02/priceindex-problem-matrix-laspeyres
sum(price[1, :] * quantity[0, :]) / sum(price[0, :] * quantity[0, :])


#---- ch02/priceindex-problem-matrix-paasche
t = 1
sum(price[t, :] * quantity[t, :]) / sum(price[0, :] * quantity[t, :])


#---- ch02/priceindex-chained-laspeyres
price = np.array([[40, 80],
                  [80, 30],
                  [70, 40],
                  [60, 55]])
quantity = np.array([[3, 6],
                     [5, 7],
                     [6, 8],
                     [8, 10]])

laspeyres = np.empty(price.shape[0])   # 価格指数の保存場所を確保

laspeyres[0] = 1.
t = 1
laspeyres[t] = laspeyres[t-1] * (sum(price[t, :] * quantity[t-1, :]) 
                                / sum(price[t-1, :] * quantity[t-1, :]))
t = 2
laspeyres[t] = laspeyres[t-1] * (sum(price[t, :] * quantity[t-1, :]) 
                                / sum(price[t-1, :] * quantity[t-1, :]))
t = 3
laspeyres[t] = laspeyres[t-1] * (sum(price[t, :] * quantity[t-1, :]) 
                                / sum(price[t-1, :] * quantity[t-1, :]))
laspeyres




