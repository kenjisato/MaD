#!/usr/bin/env python
# coding: utf-8

#---- for high-quality plots
# import matplotlib
# matplotlib.rcParams['figure.dpi'] = 196


#---- ch06/import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#---- ch06/function-1
def f(x):
    return x ** 3 - 10 * x


#---- ch06/function-2
f(3)
f(-4)


#---- ch06/function-3
a = np.array([1, 2, 3])
f(a)

#---- ch06/function-error/dnr
b = [1, 2, 3]
f(b)
#---- ch06/function-np/plot
x = np.linspace(-4, 4, 200)
plt.plot(x, f(x))
plt.show()


#---- ch06/define-multivar-func
def cd(x, y):
    alpha = 0.3
    return x**alpha * y**(1 - alpha)


#---- ch06/use-multivar-func-1
cd(2, 3)


#---- ch06/one-line
def digits(x): return np.ceil(np.log10(x + 1))

digits(np.array([102, 2020, 155550]))


#---- ch06/simple-lambda
digits2 = lambda x: np.ceil(np.log10(x + 1))
digits2(993)


#---- ch06/pandas-apply
x = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list("ABC"))
x.apply(lambda x: x ** 2)


#---- ch06/use-multivar-func-2
cd(x=2, y=3)


#---- ch06/use-multivar-func-3
cd(y=3, x=2)


#---- ch06/use-multivar-ok
cd(2, y=3)

#---- ch06/use-multivar-error/dnr
cd(x=2, 3)
#---- ch06/optional-argument
def production(k, l, a=1):
    alpha = 0.3
    return a * k**alpha * l**(1 - alpha)


#---- ch06/optional-argument-1
production(2, 3)


#---- ch06/optional-argument-2
production(2, 3, 2)


#---- ch06/arbitrary-number
def number_of_args(*args):
    return len(args)

number_of_args("First", 2, [3, 2, 1], "End")


#---- ch06/kwargs
def show_arguments(**kwargs):
    return kwargs

show_arguments(x=1, y=2, z=[1, 2])


#---- ch06/star-both
def function(*args, **kwargs):
    return (args, kwargs)

function("x", "y", a=1, b=2, c=3)


#---- ch06/call-with-star
xy = (2, 3)
cd(*xy)


#---- ch06/call-with-2stars
xydict = {'x': 2, 'y': 3}
cd(**xydict)


#---- ch06/function-print
def g(x):
    print(x)
    print("Doubling...")
    return 2 * x

g(3)

#---- ch06/function-print-error/dnr
def h(x):
    print(2 * x)
    
4 * h(3)    # 4 * 2 * 3 のつもり
#---- ch06/change-copy-hopefully
def double_1st_elem(x):
    y = x
    y[0] = 2 * x[0]
    return y

x = [1, 2, 3]
double_1st_elem(x)


#---- ch06/check-x
x


#---- ch06/change-copy-really
def double_1st(x):
    y = x[:]
    y[0] = 2 * x[0]
    return y

x = [1, 2, 3]
double_1st(x)
x


#---- ch06/scope
a = 3                # (1) a==3

def fun(x):
    a = 0            # (2) a==0
    return x + a

print(fun(0))        # (3) a==0
print(a)             # (4) a==3


#---- ch06/scope2
b = 3
def fun2(x):
    y = b
    return x + y

fun2(3)


#---- ch06/cobb-doublas-factory
def cd_factory(a):
    def F(K, L, A):
        return K**a * (A * L)**(1 - a)
    return F

cobb_douglas = cd_factory(0.33)
cobb_douglas(2, 3, 1)


#---- ch06/recursive-formula
def makeG(a, b):
    def G(y):
        return a * y + b
    return G


#---- ch06/recursive-formula-simulate
def simulate(update_rule, y0, T):
    y0 = np.asarray(y0)
    y = np.empty((T, *y0.shape))
    y[0] = y0
    for t in range(1, T):
        y[t] = update_rule(y[t-1])
    return y

G = makeG(a=0.6, b=1)
simulate(G, y0=10, T=20)


#---- ch06/randomize
def randomize(g, random):
    def randomized(*args, **kwargs):
        return g(*args, **kwargs) + random()
    return randomized

rng = np.random.default_rng(123)
Ge = randomize(G, random=rng.normal)
simulate(Ge, y0=10, T=20)


#---- ch06/solow-model
def solow(s, delta, g, n, F):
    def solow_g(x):
        K0, L0, A0 = x
        K1 = s * F(K0, L0, A0) + (1 - delta) * K0
        L1 = (1 + n) * L0
        A1 = (1 + g) * A0
        return np.array([K1, L1, A1])
    return solow_g


#---- c06/set-parameters
params = {'s': 0.3,
          'delta': 0.05,
          'g': 0.03,
          'n': 0.01,
          'F': cd_factory(0.33)}

G = solow(**params)


#---- ch06/simulate-solow
sol = pd.DataFrame(simulate(G, [2, 1, 1], 100), 
                   columns=['K', 'L', 'A'])
sol.tail(5)


#---- ch06/simulate-solow/plot
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for var, ax in zip(['K', 'A', 'L'], axes):
    sol[var].plot(ax=ax, title=var)

plt.show()

#---- ch06/reset-figsize/noinc
import matplotlib
matplotlib.rcParams.update({'figure.figsize': [12, 8]}) 
#---- ch06/small-k/plot
fig, ax = plt.subplots()

sol['k'] = sol.K / sol.A / sol.L
sol.k.plot(ax=ax)
plt.show()


#---- ch06/saving-change-initial-params
params = {'s': 0.2,
          'delta': 0.05,
          'g': 0.03,
          'n': 0.01,
          'F': cd_factory(0.33)}

G = solow(**params)
T = 20
initial = [6, 1, 1]


#---- ch6/saving-change-helper
def computeYC(frame):
    frame['Y'] = params['F'](frame.K, frame.L, frame.A)
    frame['C'] = (1 - params['s']) * frame.Y
    return frame


#---- ch06/saving-no-change
nochange = pd.DataFrame(simulate(G, initial, 3*T),
                        columns=['K', 'L', 'A'],
                        index=range(3*T))
nochange = computeYC(nochange)


#---- ch06/saving-before
before = pd.DataFrame(simulate(G, initial, T), 
                      columns=['K', 'L', 'A'],
                      index=range(T))
before = computeYC(before)
before.tail()


#---- ch06/saving-change-new-param
params['s'] = 0.3
G_new = solow(**params)
new_initial = before.iloc[-1, :3].to_numpy()


#---- ch06/saving-after
after = pd.DataFrame(simulate(G_new, new_initial, 2 * T + 1), 
                     columns=['K', 'L', 'A'],
                     index=range(T-1, 3*T))
after = computeYC(after)
saving_increased = pd.concat([before, after.iloc[1:]])


#---- ch06/saving-change/plot
saving_increased.C.plot();
nochange.C.plot();
plt.legend(['Saving rate increased', 'No change'])
plt.show()




