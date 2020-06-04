#!/usr/bin/env python
# coding: utf-8

#---- week03/list
x = [1, 2, 3]
y = [0.1, 0.2, 0.3]


#---- week03/list-sum
x + y


#---- week03/numpy
import numpy as np


#---- week03/numpy-log
np.log(np.exp(1.0))


#---- week03/vectors
x = np.array([1, 2, 3])
y = np.array([0.1, 0.2, 0.3])
x + y


#---- week03/inner
np.sum(x * y)


#---- week03/ex25-1

price00 = np.array([40, 80])
price01 = np.array([80, 30])
quantity00 = np.array([3, 6])
quantity01 = np.array([5, 7])

np.sum(price01* quantity00) / np.sum(price00 * quantity00)
# Laspeyres

np.sum(price01 * quantity01) / np.sum(price00 * quantity01)
# Paasche


#---- week03/matrix
price = np.array([[40, 80], 
                  [80, 30]])
quantity = np.array([[3, 6],
                     [5, 7]])


#---- week03/matrix-select
price[0, 1]
price[:, 0]   # : は「全部」
quantity[1, :]


#---- week03/result-array
np.ones(2)
np.zeros(2)
np.empty(2)


#---- week03/matrix-index
P = np.empty(2)
P[0] = 1.0
P[1] = P[0] * (np.sum(price[1, :] * quantity[0, :]) 
                 / np.sum(price[0, :] * quantity[0, :]))
P


#---- week03/matrix-index2
P = np.empty(2)
P[0] = 1.0
t = 1
P[t] = P[t-1] * (np.sum(price[t, :] * quantity[t-1, :]) 
                 / np.sum(price[t-1, :] * quantity[t-1, :]))
P


#---- week03/problem2/noinc

price = np.array([[40, 80],
                  [80, 30],
                  [70, 40],
                  [60, 55]])

quantity = np.array([[3, 6],
                     [5, 7],
                     [6, 8],
                     [8, 10]])

PL = np.empty(4)
PP = np.empty(4)
PL[0] = PP[0] = 1.0

t = 1
PL[t] = PL[t-1] * (np.sum(price[t, :] * quantity[t-1, :]) 
                  / np.sum(price[t-1, :] * quantity[t-1, :]))
PP[t] = PP[t-1] * (np.sum(price[t, :] * quantity[t, :]) 
                  / np.sum(price[t-1, :] * quantity[t, :]))

t = 2
PL[t] = PL[t-1] * (np.sum(price[t, :] * quantity[t-1, :]) 
                  / np.sum(price[t-1, :] * quantity[t-1, :]))
PP[t] = PP[t-1] * (np.sum(price[t, :] * quantity[t, :]) 
                  / np.sum(price[t-1, :] * quantity[t, :]))

t = 3
PL[t] = PL[t-1] * (np.sum(price[t, :] * quantity[t-1, :]) 
                  / np.sum(price[t-1, :] * quantity[t-1, :]))
PP[t] = PP[t-1] * (np.sum(price[t, :] * quantity[t, :]) 
                  / np.sum(price[t-1, :] * quantity[t, :]))


#---- week03/problem2/plot
import matplotlib.pyplot as plt
plt.plot(PL, label = 'Laspeyres')
plt.plot(PP, label = 'Paasche')
plt.legend()
plt.show()




