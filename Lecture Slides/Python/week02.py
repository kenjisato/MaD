#!/usr/bin/env python
# coding: utf-8

#---- week02/point/graphics

import pandas as pd
import matplotlib.pyplot as plt

pwt = pd.read_stata('../Raw Data/pwt91.dta')
jpn = pwt[pwt.country == "Japan"].copy()
jpn.rgdpo = jpn.rgdpo / 1000

jpn2010 = jpn[jpn.year == 2010]
ax = jpn2010.plot(x='year', y='rgdpo', marker='x')
_ = ax.set_ylabel("Real GDP (output) in 2011USD (PPP)")

plt.show()


#---- week02/line/graphics

ax = jpn.plot(x='year', y='rgdpo', color='#ff7f0e')
ax.plot(jpn2010.year, jpn2010.rgdpo, color='#1f77b4', marker='x')
_ = ax.set_ylabel("Real GDP (output) in 2011USD (PPP)")

plt.show()


#---- week02/growth/graphics

jpn['growth'] = jpn.rgdpo.pct_change() * 100
ax = jpn.plot(x = 'year', y = 'growth')
_ = ax.set_ylabel("Real GDP growth (%)")

plt.show()


#---- week02/exa1
y0, y1, y2, y3 = 500, 550, 600, 650


#---- week02/exa2
g1, g2, g3, g4, g5 = 0.02, 0.05, 0.01, 0.04, 0.03

