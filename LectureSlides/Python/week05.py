#!/usr/bin/env python
# coding: utf-8

# # Week 5 スライド

# ## NumPy Data

# In[1]:


#---- week05/practice
import numpy as np

rng = np.random.default_rng(100)   # 100 は乱数の種
x = rng.choice(range(100, 500), 15)
np.mean(x)
np.median(x)
np.quantile(x, 0.9)
x > 300
x[x > 300]


# In[2]:


#---- week05/tf-vector
x > 400
x[x > 400]


# In[3]:


#---- week05/tf-sum
True + True + False
True + False + False + True + True


# In[4]:


#---- week05/tf-count
np.sum(x > 400)


# In[5]:


#---- week05/tf-ratio
np.mean(x > 400)


# In[6]:


#---- week05/median
np.median(x)


# In[7]:


#---- week05/quantile
np.quantile(x, 0.9)    # 下から90% の値


# ## 相対的貧困

# In[8]:


#---- week05/disposable-income
import pandas as pd
frame = pd.DataFrame({
    'household': list('AAABBCD'),
    'income': [400, 300, 0, 1000, 0, 250, 150.]
}, index=range(1, 8))
frame


# In[9]:


#---- week05/disposable-income2
income = (frame.groupby('household')
 .transform(lambda x: x.sum() / np.sqrt(x.size)))
income


# In[10]:


#---- week05/less-than-rpl
income < np.median(income) / 2


# In[11]:


#---- week05/relative-poverty
np.mean(income < np.median(income) / 2) * 100


# ## Gini 係数

# In[12]:


#---- week05/gini-data-gen
xlow = rng.choice(np.arange(10, 50.), 10)
xhigh = rng.choice(np.arange(80, 200.), 10)
x = np.r_[xlow, xhigh]
x


# In[13]:


#---- week05/gini-sorted
y = np.sort(x)   # Step 1
y


# In[14]:


#---- week05/gini-cum-freq
Y = np.r_[0, y.cumsum()] / y.sum()  # Step 2, 3
Y


# In[15]:


#---- week05/gini-formula
gini = 1 - (2 * np.sum(Y) - 1) / y.size   # Step 4, 5, 6
gini


# ## Top percentile share

# In[16]:


#---- week05/top-percentile-data
x


# In[17]:


#---- week05/top-percentile-threshold
np.quantile(x, 0.99)


# In[18]:


#---- week05/top-percentile-share
np.sum(x[x > np.quantile(x, 0.99)]) / np.sum(x)


# In[19]:


#---- END


# ## 参考: Python のループ・ベクトル計算
# 
# 500000個の正規乱数を発生させて，各要素の絶対値を取る簡単な計算をする。
# 
# 1. `r_abs1` はループの中で if-else を使って1つずつ処理する。もっとも汎用性が高い。一見すると無駄も少ないように見える。
# 1. `r_abs2` は `np.where` を使ってベクトル化する。汎用性の高い方法。
# 1. `r_abs3` は `np.abs` を使った例，効率はよさそうだけど汎用性が低い。

# In[20]:


r = rng.normal(size=(500000))
r_abs1 = np.empty_like(r)


# #### Case 1

# In[21]:


get_ipython().run_cell_magic('timeit', '', 'for i in range(r.size):\n    rr = r[i]\n    if rr >= 0:\n        r_abs1[i] = rr\n    else:\n        r_abs1[i] = -rr')


# #### Case 2

# In[22]:


get_ipython().run_cell_magic('timeit', '', 'r_abs2 = np.where(r >= 0, r, -r)')


# #### Case 3

# In[23]:


get_ipython().run_cell_magic('timeit', '', 'r_abs3 = np.abs(r)')


# #### 結果
# 
# Case 2 は Case 1 より 100くらいはやい。Case 3 は Case 2 より 8倍くらい早い。一般的な教訓として覚えておこう。
# 
# - 特定のケースを処理するために作られた関数は実行速度が早い。必要なループ処理が Fortran/C で書かれている。
# - ベクトル計算は無駄な計算をしている（例えば，全要素に対して `-r` を計算している）ようだけど，ループで処理するよりは断然まし。
# - 本当にその for/while が必要かどうかを吟味する。

# In[ ]:




