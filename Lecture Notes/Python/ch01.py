#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('matplotlib', 'inline')


#---- ch01/plot-log-approx/graphics
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 0.5, 200)
plt.plot(x, np.log(1 + x), 'k', label='y = log(1 + x)')
plt.plot(x, x, 'k--', label='y = x')
plt.legend()
plt.margins(tight=True)
plt.show()


#---- ch01/plot-compounding/graphics
t = np.arange(30)
plt.plot(t, 1.06 ** t * 100, 'k', label='$1.06^t \\times 100$')
plt.plot(t, 100 + 6 * t, 'k--', label='$100 + 6t$')
plt.xlabel('t')
plt.legend()
plt.margins(tight=True)
plt.show()


#---- ch01/simple-math
10 + 10.5
3 - 5
2 * 3
6 / 4
2 ** 10


#---- ch01/division-math
100 // 3
100 % 3


#---- ch01/unary-operator
-3 * 2
2.5 * -2


#---- ch01/paren1
2.5 * (-2)


#---- ch01/operator-precedence1
3 + 1 * 2
(3 + 1) * 2
6 / 2 / 3


#---- ch01/operator-precedence2
1 + - 1 * - 3 ** 2
1 + (- 1) * (- (3 ** 2))


#---- ch01/long-expression
(1 + 2 + 3 + 4 + 5 
 + 6 + 7 + 8 + 9 + 10)


#---- ch01/long-expression2
1 + 2 + 3 + 4 + 5  + 6 + 7 + 8 + 9 + 10


#---- ch01/assignment
x = 10
x


#---- ch01/print
print(x)


#---- ch01/var-calc
x * 10


#---- ch01/variables1
g = 0.02
y0 = 500
t = 3
yt = (1 + g) ** t * y0
yt


#---- ch01/variables2
growth_rate = 0.02
GDP_0 = 500
years = 3
GDP_3 = (1 + growth_rate) ** years * GDP_0
GDP_3


#---- ch01/float-method
1.5.as_integer_ratio()


#---- ch01/load-numpy
import numpy as np


#---- ch01/numpy-log
np.log(10)
np.exp(1)


#---- ch01/numpy-constants
np.pi
np.e


#---- ch01/growth-rate

y0 = 300
y1 = 306
np.log(y1) - np.log(y0)
(y1 - y0) / y0




