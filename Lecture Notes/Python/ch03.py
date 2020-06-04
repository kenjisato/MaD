#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('matplotlib', 'inline')


#---- ch03/plot-lorenz/graphics
import numpy as np
import matplotlib.pyplot as plt

# Fix random numbers
np.random.seed(101)

# Income
y = np.random.choice(range(1, 10), 7)

Y = np.r_[0, np.sort(y).cumsum() / y.sum()]
X = np.linspace(0, 1, y.size + 1)

fig, ax = plt.subplots(1, 1)
ax.plot(X, Y, 'k')
ax.plot(X, X, 'k--')
ax.fill_between(X, X, Y, color='gray', alpha=0.3)
ax.set_aspect('equal')

plt.show()


#---- ch03/def-functions/dnr
def f(): print("f is called.")
def g(): print("g is called.")
def h(): print("h is called.")


#---- ch03/sequential/dnr
f()
g()
h()


#---- ch03/no-loop/dnr
f()    # 0回目
f()    # 1回目
f()    # 2回目
g()


#---- ch03/for-loop/dnr
for i in [0, 1, 2]:
    f()

g()


#---- ch03/for-loop-equiv/dnr
i = 0
f()

i = 1
f()

i = 2
f()

g()


#---- ch03/for-loop-print
for i in [0, 1, 2]:
    print(i)


#---- ch03/for-with-range
for i in range(3):
    print(i)


#---- ch03/boolean
True


False


#---- ch03/boolean-and
[True and True, True and False, False and True, False and False]


#---- ch03/boolean-or
[True or True, True or False, False or True, False or False]


#---- ch03/boolean-not
[not True, not False]


#---- ch03/boolean-inequality
[1 < 2, 1 <= 2, 1 == 2, 1 > 2, 1 >= 2]


#---- ch03/boolean-addition
True + True + False


#---- ch03/compare-real-numbers
0.1 + 0.3 + 0.6 == 1.0


0.3 + 0.6 + 0.1 == 1.0


#---- ch03/compare-real-numbers2
import numpy as np
np.allclose(0.1 + 0.3 + 0.6, 1.0, rtol=1e-15)


#---- ch03/condition/noinc
condition = False
condition1 = True
condition2 = False


#---- ch03/while-loop-equiv/dnr
while condition:
    f()


#---- ch03/while-loop/dnr
i = 0
while i < 3:
    f()
    i += 1
    
g()


#---- ch03/inf-loop/error
raise(BaseException('Comment out before executing this cell.'))

#---- ch03/inf-loop/dnr
while True:
    print(i)
    i += 1


#---- ch03/if/dnr
if condition:
    f()


#---- ch03/if-else/dnr
if condition:
    f()
else:
    g()


#---- ch03/if-elif-else/dnr
if condition1:
    f()
elif condition2:
    g()
else:
    h()


#---- ch03/if-odds-total
total = 0
for i in range(1, 101):
    if i % 2 == 1:
        total += i

total


#---- ch03/if-odds-total-comprehension
sum(i for i in range(1, 101) if i % 2 == 1)


#---- ch03/boolean-array
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
x < y


#---- ch03/boolean-array2
x[x < y]


#---- ch03/set-random/noinc
np.random.seed(101)


#---- ch03/boolean-random
z = np.random.random(1000)
np.mean(z > 0.95)


#---- ch03/gdp-data
price = np.array([[100, 100, 100],
                  [101, 99, 103],
                  [100, 98, 104],
                  [99, 97, 106.]])
quantity = np.array([[1000, 2000, 500],
                     [980, 1980, 510],
                     [1010, 1990, 520],
                     [1005, 2005, 530.]])


#---- ch03/gdp-nominal
nominal_gdp = np.sum(price * quantity, axis=1)
nominal_gdp


#---- ch03/gdp-deflator
dfl = np.empty_like(nominal_gdp)
dfl[0] = 1.
for t in range(1, len(dfl)):
    dfl[t] = dfl[t-1] * (np.sum(price[t, :] * quantity[t, :]) 
                            / np.sum(price[t-1, :] * quantity[t, :]))
    
dfl * 100


#---- ch03/gdp-real
real_gdp = nominal_gdp / dfl
real_gdp


#---- ch03/toy-example
x0 = np.array([10, 20, 15])
x1 = np.array([9, 22, 16])
contribution = (x1 - x0) / x0.sum() * 100
contribution


#---- ch03/contribution-data
value = price * quantity
value


#---- ch03/contribution-nominal-gdp
np.allclose(nominal_gdp, np.sum(value, axis=1), rtol=1e-15)


#---- ch03/nominal-growth
np.diff(nominal_gdp, prepend=np.nan) / np.roll(nominal_gdp, shift=1)


#---- ch03/nominal-contribution
contribution = (np.diff(value, prepend=np.nan, axis=0) 
                / np.roll(nominal_gdp, shift=1).reshape(4, 1)) * 100
contribution


#---- ch03/contribution-sum
contribution.sum(axis=1)


#---- ch03/median
x = np.array([3, 6, 10, 14, 3, 2, 1, 1])
np.median(x)


#---- ch03/relative-poverty
x < np.median(x) / 2


#---- ch03/relative-poverty-rate
np.mean(x < np.median(x) / 2)


#---- ch03/gini-random-data
x = np.random.choice(np.arange(30.), 10)
x


#---- ch03/gini-sorted-data
y = np.sort(x)
y


#---- ch03/gini-cum-income
Y = np.r_[0, y.cumsum()] / y.sum()
Y


#---- ch03/gini-formula
gini = 1 - (2 * np.sum(Y) - 1) / y.size
gini


#---- ch03/top-1percent
x[x >= np.quantile(x, 0.99)]


#---- ch03/top-1percent-share
x[x >= np.quantile(x, 0.99)].sum() / x.sum()




