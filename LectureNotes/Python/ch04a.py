#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import numpy.linalg as LA


file = 'Data/000629595-sheet5.xlsx'

nsector = 37

# B列から産業部門を取得する
sectors = pd.read_excel(file, usecols='B', header=None, 
                        skiprows=4, nrows=nsector, squeeze=True)
sectors.name = None
sectors


# 中間需要のデータを取得する
iotable = pd.read_excel(file, usecols='C:AM', header=None,
                        skiprows=4, nrows=nsector)
iotable


# 列名の変更
iotable.columns = sectors
iotable.columns.name = '需要部門'

# 行名の変更
iotable.index = sectors
iotable.index.name = '供給部門'

iotable


# 域内最終需要
final_demand = pd.read_excel(file, usecols='AU', header=None, 
                             skiprows=4, nrows=nsector, squeeze=True, 
                             names = ["域内最終需要"])
final_demand.index = sectors
final_demand


# 移輸出
exports = pd.read_excel(file, usecols='AW', header=None, 
                        skiprows=4, nrows=nsector, squeeze=True, 
                        names = ['移輸出'])
exports.index = sectors
exports


# 移輸入
imports = pd.read_excel(file, usecols='BD', header=None, 
                        skiprows=4, nrows=nsector, squeeze=True, 
                        names = ['移輸入'])
imports = -imports
imports.index = sectors
imports


# 域内生産
production = pd.read_excel(file, usecols='BF', header=None, 
                           skiprows=4, nrows=nsector, squeeze=True, 
                           names = ['域内生産'])
production.index = sectors
production


# intermediate demand
intermediate_demand = iotable.sum(axis=1)
intermediate_demand


intermediate_demand + final_demand + exports - imports == production


value_added = production - iotable.sum(axis=0)
value_added


input_coeff = iotable / production
input_coeff


import_coeff = pd.DataFrame(np.diag(imports / (intermediate_demand + final_demand)))
import_coeff.columns = import_coeff.index = sectors
import_coeff


inv_table = pd.DataFrame(LA.inv(np.eye(len(sectors)) - (np.eye(len(sectors)) - import_coeff) @ input_coeff))
inv_table.columns = inv_table.index = sectors
inv_table


100_000


demand_shock = pd.Series([0.0] * nsector, index=sectors)
demand_shock['情報通信'] = 1_000_000_000.0

demand_shock


np.sum(inv_table @ (np.eye(nsector) - import_coeff) @ demand_shock) / 1_000_000


A = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
A.index = ['a', 'b']
A


b = pd.Series([0.1, 0.01])
b.index = ['a', 'b']
b


A / b




