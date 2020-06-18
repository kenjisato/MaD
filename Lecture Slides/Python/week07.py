#!/usr/bin/env python
# coding: utf-8
#---- week07/install/dnr
!conda install -y pandas-datareader
#---- week07/prepare
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt


#---- week07/array2frame
rng = np.random.default_rng(123)
x = rng.choice(range(30), size=(20, 3))
df = pd.DataFrame(x, columns=['A', 'B', 'C'], 
                  index=range(2000, 2020))
df.tail(5)


#---- week07/get-column/dnr
df.A
df['B']
df[['A', 'C']]


#---- week07/get-row
df.loc[2000:2007, ['A', 'C']]


#---- week07/dict
d = {'x': 10, 'y': [10, 20], 'z': ['USA', 'JPN'], 100: 'OPU'}
d
d['x']
d[100]


#---- week07/dict2frame
frame = pd.DataFrame({'a': rng.normal(size=20),
                      'b': rng.normal(size=20)})


#---- week07/plot1/plot
frame.plot()
plt.show()


#---- week07/plot2/plot
frame.plot.scatter(x='a', y='b')
plt.show()





#---- END



