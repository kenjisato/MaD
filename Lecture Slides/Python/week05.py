#!/usr/bin/env python
# coding: utf-8

#---- week05/practice
import numpy as np

rng = np.random.default_rng(100)   # 100 は乱数の種
x = rng.choice(range(100, 500), 15)
np.mean(x)
np.median(x)
np.quantile(x, 0.9)
x > 300
x[x > 300]


#---- week05/tf-vector
x > 400
x[x > 400]


#---- week05/tf-sum
True + True + False
True + False + False + True + True


#---- week05/tf-count
np.sum(x > 400)


#---- week05/tf-ratio
np.mean(x > 400)


#---- week05/median
np.median(x)


#---- week05/quantile
np.quantile(x, 0.9)    # 下から90% の値


#---- week05/disposable-income
import pandas as pd
frame = pd.DataFrame({
    'household': list('AAABBCD'),
    'income': [400, 300, 0, 1000, 0, 250, 150.]
}, index=range(1, 8))
frame


#---- week05/disposable-income2
income = (frame.groupby('household')
 .transform(lambda x: x.sum() / np.sqrt(x.size)))
income


#---- week05/less-than-rpl
income < np.median(income) / 2


#---- week05/relative-poverty
np.mean(income < np.median(income) / 2) * 100


#---- week05/gini-data-gen
xlow = rng.choice(np.arange(10, 50.), 10)
xhigh = rng.choice(np.arange(80, 200.), 10)
x = np.r_[xlow, xhigh]
x


#---- week05/gini-sorted
y = np.sort(x)   # Step 1
y


#---- week05/gini-cum-freq
Y = np.r_[0, y.cumsum()] / y.sum()  # Step 2, 3
Y


#---- week05/gini-formula
gini = 1 - (2 * np.sum(Y) - 1) / y.size   # Step 4, 5, 6
gini


#---- week05/top-percentile-data
x


#---- week05/top-percentile-threshold
np.quantile(x, 0.99)


#---- week05/top-percentile-share
np.sum(x[x > np.quantile(x, 0.99)]) / np.sum(x)


#---- END


r = rng.normal(size=(500000))
r_abs1 = np.empty_like(r)


get_ipython().run_cell_magic('timeit', '', 'for i in range(r.size):\n    rr = r[i]\n    if rr >= 0:\n        r_abs1[i] = rr\n    else:\n        r_abs1[i] = -rr')


get_ipython().run_cell_magic('timeit', '', 'r_abs2 = np.where(r >= 0, r, -r)')


get_ipython().run_cell_magic('timeit', '', 'r_abs3 = np.abs(r)')




