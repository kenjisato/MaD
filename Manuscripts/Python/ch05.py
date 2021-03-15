#!/usr/bin/env python
# coding: utf-8

#---- for high-quality plots
# import matplotlib
# matplotlib.rcParams['figure.dpi'] = 196


#---- ch05/growth-graph/plot

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(100)
y = (1 + 0.02) ** t
plt.plot(t, y)
plt.show()


#---- ch05/growth-graph-log/plot
plt.plot(t, np.log(y))
plt.show()


#---- ch05/growth-change/plot
y2 = np.empty_like(y)
y2[:50] = (1 + 0.02) ** t[:50]
y2[50:] = y2[49] * (1 + 0.04) ** (t[50:] - 49)
plt.plot(t, y2)
plt.show()


#---- ch05/growth-change-log/plot
plt.plot(t, np.log(y2))
plt.show()


#---- ch05/growth-log-scale/plot
plt.plot(t, y2)
plt.yscale('log')
plt.show()


#---- ch05/string-1
s1 = "Hello."
s1


#---- ch05/string-2
s2 = 'こんにちは'
s2


#---- ch05/string-3
s1[0]
s1[1:3]
s1[-1]


#---- ch05/string-list
list(s2)


#---- ch05/string-for
for i, s in enumerate(s1):
    print(s * (i + 1))


#---- ch05/f-string
x, y = 10, 20
f"{x} + {y} = {x + y}"


#---- ch05/f-string-format
f"{x} / ({x} + {y}) ≒ {x / (x + y):.2f}"


#---- ch05/define-dict
d = {1: 100, 'a': 200, 'x': [1, 2]}
d


#---- ch05/read-dict
d[1]
k = 'a'
d[k]


#---- ch05/loop-dict
for key in d:
    print(key)


#---- ch05/loop-dict2
for k, v in d.items():
    print(f"{k} : {v}")


#---- ch05/pandas-no-indices
import pandas as pd
x = np.arange(12.0).reshape(4, 3)
pd.DataFrame(x)


#---- ch05/pandas-with-indices
frame = pd.DataFrame(x, columns=['a', 'b', 'c'], 
                     index=pd.PeriodIndex(range(2000, 2004), freq='A'))
frame


#---- ch05/pandas-define-with-dict
pd.DataFrame({'a': [0.0, 3.0, 6.0, 9.0],
              'b': [1.0, 4.0, 7.0, 10.0],
              'id': list('xyzw')},
              index=range(2000, 2004))


#---- ch05/pandas-diff
frame.diff()


#---- ch05/pandas-pct-change
frame.pct_change().dropna()


#---- ch05/pandas-get-columns
frame.a
frame['b']
frame[['a', 'c']]


#---- ch05/pandas-get-rows
frame.loc['2000':'2002', :]


#---- ch05/pandas-add-column
frame['d'] = frame.b * frame.c + 10
frame


#---- ch05/pandas-plot/plot
frame.plot(y = ['a', 'd'])
plt.show()


#---- ch05/pandas-scatter/plot
frame.plot.scatter(x='a', y='d', s=10 * frame.b ** 2)
plt.show()


#---- ch05/pandas-bar/plot
frame.plot.bar()
plt.show()


#---- ch05/pandas-barh/plot
ax = frame.plot.barh(stacked=True)
ax.invert_yaxis()
plt.show()


#---- ch05/pandas-datareader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr


#---- ch05/pandas-fred-gdp
gdp = pdr.get_data_fred(['GDPPOT', 'GDPC1'], 
                        start='1960-01-01', end='2020-04-01')
gdp


#---- ch05/pandas-fred-gdp/plot
gdp[['GDPPOT', 'GDPC1']].plot()
plt.show()


#---- ch05/pandas-fred-gdp-gap
gdp['gap'] = gdp['GDPC1'] - gdp['GDPPOT']
gdp['rgap'] = gdp['gap'] / gdp['GDPPOT']
gdp


#---- ch05/pandas-fred-price
price = pdr.get_data_fred('CPIAUCSL', 
                          start='1960-01-01', end='2020-04-01')
price


#---- ch05/pandas-fred-inflation/plot
price['inflation'] = price.CPIAUCSL.pct_change() * 12
price.inflation.plot()
plt.show()


#---- ch05/pandas-fred-ma
price['ma3'] = price.inflation.rolling(3, center=True).mean()
price['ma9'] = price.inflation.rolling(9, center=True).mean()
price


#---- ch05/pandas-fred-ma-plot/plot
ax = price.inflation.plot(alpha=0.2)
price[['ma3', 'ma9']].plot(ax = ax)
plt.show()


#---- ch05/wb-gdp
from pandas_datareader import wb
gdp = wb.download(indicator='NY.GDP.PCAP.CD', country='all',
                  start=1960, end=2010)
gdp


#---- ch05/wb-gdp-pivot
gdp_pivot = gdp.reset_index()
gdp_pivot['NY.GDP.PCAP.CD'] = np.log(gdp_pivot['NY.GDP.PCAP.CD'])
gdp_pivot = gdp_pivot.pivot(index='year', columns='country', 
                            values='NY.GDP.PCAP.CD')
gdp_pivot.index = gdp_pivot.index.astype('uint64')


#---- ch05/wb-gdp-pivot/dnr
gdp_pivot


#---- ch05/wb-gdp-density/plot
years = [1960, 1980, 2000, 2010]
fig, ax = plt.subplots(1)
for year in years:
    gdp_pivot.loc[year].dropna().plot.density(ax=ax)
    
ax.legend(years)
ax.set_xlabel('Log GDP per capita')
plt.show()


#---- ch05/import2/noinc
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt


#---- ch05/fred-gdp-read/noinc
fred = pdr.get_data_fred(['GDPPOT', 'GDPC1', 'PCEPI', 'NROU', 'UNRATE'], 
                         start='1960', end='2020-04-01')
fred


#---- ch05/fred-gdp/graphics
ax = fred[['GDPPOT', 'GDPC1']].dropna().plot()
ax.set_xlabel('Quarter')
ax.set_ylabel('log Real GDP (Billion 2012USD)')
ax.set_yscale('log')
ax.legend(['Potential GDP', 'Real GDP'])
plt.show()


#---- ch05/gdp-gap/graphics
fred["GAP"] = (fred.GDPC1 - fred.GDPPOT) / fred.GDPPOT
fred["Inflation"] = fred.PCEPI.pct_change().shift(-1) * 12

GAP = fred.GAP.dropna()

ax = GAP.plot(color=['C0', 'k'])
x = np.linspace(*ax.get_xlim(), GAP.shape[0])
ylim = ax.get_ylim()
ax.hlines([0.0], xmin=x[0], xmax=x[-1], linestyle=':')
ax.fill_between(x, 0, 1, where=(GAP < 0), alpha=0.1, color='k',
                transform=ax.get_xaxis_transform())
ax.set_ylim(*ylim)
ax.set_xlabel('Quarter')
ax.set_ylabel('GDP Gap / Potential GDP')
plt.show()


#---- ch05/fred-umemployment/graphics
fig, ax = plt.subplots(1)
fred[['UNRATE', 'NROU']].dropna().plot(ax=ax)
x = np.linspace(*ax.get_xlim(), GAP.shape[0])
ax.fill_between(x, 0, 1, where=(GAP < 0), alpha=0.1, color='k',
                transform=ax.get_xaxis_transform())
ax.legend(['Unemployment Rate', 'Natural Rate of Unemployment'])
plt.show()


#---- ch05/fred-inflation/graphics
fig, ax = plt.subplots(1)
fred['Inflation'].dropna().rolling(12, center=True).mean().plot(ax=ax)
x = np.linspace(*ax.get_xlim(), GAP.shape[0])
ylim = ax.get_ylim()
ax.fill_between(x, 0, 1, where=(GAP < 0), alpha=0.1, color='k',
                transform=ax.get_xaxis_transform())
ax.hlines([0.0], xmin=ax.get_xlim()[0], 
          xmax=ax.get_xlim()[1], linestyle=':')
ax.set_ylim(*ylim)
ax.legend(['Inflation (12m Rolling Mean)'])
plt.show()


#---- END




