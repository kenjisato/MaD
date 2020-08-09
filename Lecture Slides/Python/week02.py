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


#---- week02/var
x = 10
y = x
a, b = 1, 2.3
hello = "Good bye"


#---- week02/use-var
x * b
print(hello)


#---- week02/hidden-name/dnr
x y = 5      # 空白を含む
4a = 10      # 数字から始まる
x-y = 0      # ハイフンを使っている
u*z = x      # 記号はほとんど使えない


#---- week02/usable-name/dnr
my_name = "Jack Bauer"    # アンダースコアは使える
点数 = 100                # ユニコード文字も一部使える 


#---- week02/exa1
y0, y1, y2, y3 = 500, 550, 600, 650


#---- week02/exa2
g1, g2, g3, g4, g5 = 0.02, 0.05, 0.01, 0.04, 0.03

