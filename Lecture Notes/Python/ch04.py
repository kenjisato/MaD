#!/usr/bin/env python
# coding: utf-8

#---- ch04/import
import numpy as np
import matplotlib.pyplot as plt


#---- for high-quality plots
# import matplotlib
# matplotlib.rcParams['figure.dpi'] = 196


#---- ch04/3d-array-zero
T, d = 3, 2
x = np.zeros((T, d, 1))
x


#---- ch04/3d-array-initial
x[0] = np.array([[1],
                 [2]])
x


#---- ch04/transition-matrix
A = np.array([[0.5, -0.2],
              [1.0, 0.0]])
A


#---- ch04/simulation
for t in range(1, T):
    x[t] = A @ x[t-1]

x


#---- ch04/reshape
x.shape = (T, d)
x


#---- ch04/import-linalg
import scipy.linalg as LA
import matplotlib.pyplot as plt


#---- ch04/define-A1
A1 = np.array([[0.8, 0.1],
               [0.5, 1.2]])


#---- ch04/eigen-A1
E, V = LA.eig(A1)
np.abs(E)


#---- ch04/unstable-A1/plot
N = 50
x = np.zeros(N)

An = np.eye(A1.shape[0])
x[0] = np.sum(np.abs(An))       # Σ|a_n|
for n in range(1, N):
    An = An @  A1
    x[n] = np.sum(np.abs(An))   # Σ|a_n| 
    
plt.plot(x)


#---- ch04/define-A2
A2 = np.array([[0.7, -0.1],
              [0.3, 1.05]])

E, V = LA.eig(A2)
np.abs(E)


#---- ch04/stable-A2/graphics
N = 50
x = np.zeros(N)

An = np.eye(A2.shape[0])
x[0] = np.sum(np.abs(An))       # Σ|a_n|
for n in range(1, N):
    An = An @  A2
    x[n] = np.sum(np.abs(An))   # Σ|a_n| 
    
plt.plot(x)


#---- ch04/inverse-formula
I = np.eye(A2.shape[0])
S = I
for n in range(1, 200):
    S = I + A2 @ S
    
np.allclose((I - A2) @ S, I)


#---- ch04/ar-coeff
A = np.array([[0.6, 0.3],
              [1.0, 0.0]])


#---- ch04/ar-eig
E, V = LA.eig(A)
np.abs(E)


#---- ch04/ar-coeff-other
B = np.array([[1.0],
              [0.0]])
C = np.array([[1.0, 0.0]])
x0 = np.array([[0.0],
               [0.0]])


#---- ch04/ar-noise
rng = np.random.default_rng(1234)    # 124 は再現性のため
rng.normal(loc=0, scale=1.0, size=(3, 1, 1))


#---- ch04/ar-simulation
T, d = 300, 2
x = np.empty((T, d, 1))
y = np.empty((T, 1, 1))
eps = rng.normal(loc=0, scale=1.0, size=(T, 1, 1))

x[0] = x0
y[0] = C @ x[0]

for t in range(1, T):
    x[t] = A @ x[t-1] + B @ eps[t]
    y[t] = C @ x[t]
    
y.shape = (T, )
y[:5]


#---- ch04/ar-plot/plot
plt.plot(y)


#---- ch04/import-tsa
import statsmodels.tsa.api as tsa


#---- ch04/acf/plot
tsa.graphics.plot_acf(y)
plt.show()


#---- ch04/pacf/plot
tsa.graphics.plot_pacf(y)
plt.show()


#---- ch04/ar-estimate
mod = tsa.SARIMAX(y, order=(2, 0, 0))
result = mod.fit() 


#---- ch04/ar-params
result.params


#---- ch04/ar-summary/dnr
result.summary()




