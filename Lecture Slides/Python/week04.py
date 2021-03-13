#!/usr/bin/env python
# coding: utf-8

# # Week 4 スライド

# ## NumPy array

# In[1]:


#---- week04/import
import numpy as np


# In[2]:


#---- week04/arange
A = np.arange(24)
A


# In[3]:


#---- week04/shape
A.shape


# In[4]:


#---- week04/reshape1
A.shape = (3, 8)


# In[5]:


#---- week04/reshape2
A


# In[6]:


#---- week04/reshape3
A.shape = (2, 3, 4)
A


# In[7]:


#---- week04/axis-sum
A.shape = (4, 6)
A.sum()          # (4, 6) -> ()
A.sum(axis=0)    # (4, 6) -> (6,)
A.sum(axis=1)    # (4, 6) -> (4,)


# ## for

# In[8]:


#---- week04/for-loop1
for i in range(5):
    print(i ** 3)


# ## GDP

# In[9]:


#---- week04/gdp-data
price = np.array([[100, 100, 100],
                  [101, 99, 103],
                  [100, 98, 104],
                  [99, 97, 106.]])

quantity = np.array([[1000, 2000, 500],
                     [980, 1980, 510],
                     [1010, 1990, 520],
                     [1005, 2005, 530.]])


# In[10]:


#---- week04/gdp-value
price * quantity


# In[11]:


#---- week04/gdp-nominal-def/noinc
NGDP = np.sum(price * quantity, axis=1)


# In[12]:


#---- week04/gdp-nominal-show
NGDP


# In[13]:


#---- week04/gdp-real-no-for
GDP = np.empty(price.shape[0])  # 行数 = 年数

GDP[0] = np.sum(price[0, :] * quantity[0, :])
t = 1
GDP[t] = GDP[t-1] * (np.sum(price[t-1, :] * quantity[t, :]) 
                    / np.sum(price[t-1, :] * quantity[t-1, :]))
t = 2
# .... continue


# In[14]:


#---- week04/gdp-real
T = price.shape[0]  # 行数 = 年数
GDP = np.empty(T)

GDP[0] = np.sum(price[0, :] * quantity[0, :])
for t in range(1, T):
    GDP[t] = (GDP[t-1] 
               * (np.sum(price[t-1, :] * quantity[t, :]) 
                / np.sum(price[t-1, :] * quantity[t-1, :])))

GDP


# In[15]:


#---- week04/contribution-data
expenditure = np.array([[298.88, 101.56, 132.33, 91.43, -92.62],
                        [299.05, 102.28, 139.39, 92.87, -94.62]])


# In[16]:


#---- week04/contribution-diff
diff = np.diff(expenditure, prepend=np.nan, axis=0)
diff


# In[17]:


#---- week04/contribution-gdp
gdp = expenditure.sum(axis=1)
gdp


# In[18]:


#---- week04/contribution-gdp-shifted
gdp_shift = np.r_[np.nan, gdp[:-1]]
gdp_shift.shape = (2, 1)
gdp_shift


# In[19]:


#---- week04/contribution
contribution = diff / gdp_shift


# In[ ]:





# In[ ]:




