#!/usr/bin/env python
# coding: utf-8

# In[61]:


pip install pandas


# In[62]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[63]:


dg1 = pd.read_csv('data/data_group_1.csv')
dg2 = pd.read_csv('data/data_group_2.csv')
dg3 = pd.read_csv('data/data_group_3.csv')


# In[64]:


frames = [dg1, dg2, dg3]

df = pd.concat(frames)
df.info()


# In[65]:


df.describe()


# I've loaded the data in and checked the data types and size of the overall joint dataset.

# In[66]:


df.isna().any()


# In[67]:


df[df.duplicated()]


# I've checked for any null values in the dataset and duplicate values, but can't find any. I've also tried to check manually but can't see any null values (obviously duplicates are more difficult).

# In[68]:


df = df.sort_values(by=["timestamp","turbine_id"])
df.head(15)


# As the data sets are joined together but not sorted together, I've sorted the data on the timestamp and turbine_id values. This shows all 15 turbines next to each other.

# In[69]:


sns.boxplot(data=df, x="turbine_id", y="wind_speed")


# In[70]:


sns.boxplot(data=df, x="turbine_id", y="wind_direction")


# In[71]:


sns.boxplot(data=df, x="turbine_id", y="power_output")


# I've checked here for any outlier values in the wind_speed, wind_direction and power_output columns but can't see any. The values for wind_direction are between 0 and 360, with the assumption that this is the angle of the wind.

# In[72]:


df['timestamp'] = df['timestamp'].apply(pd.to_datetime)
df_avg = df.groupby([df['timestamp'].dt.date, 'turbine_id']).agg({'power_output':[np.min,np.max,np.mean,np.median,np.std]})
df_avg.head()


# Here I'm compiling the daily values, the min-max values and averages, along with the standard deviation of each value. None of the turbines have a standard deviation above 2, so it's not necessary to flag any.

# In[73]:


df_avg.to_csv("daily_avg.csv", index=True)
df.to_csv("clean.csv", index=True)


# Here I'm outputting the cleaned data and the daily averages data to seperate files.

# In[ ]:




