#!/usr/bin/env python
# coding: utf-8

# #                       Uber Tripe Analysis 

# By analyzing Uber trips, we can draw many patterns like which day has the highest and the lowest trips or the busiest hour for Uber and many other patterns. The dataset I’m using here is based on Uber trips from New York, a city with a very complex transportation system with a large residential community.
# 
# The dataset contains data of about 4.5 million uber pickups in New York City from April to September and 14.3 million pickups from January to June 2015. You can do so much more with this dataset rather than just analyzing it. But for now, in the section below, I will take you through Uber Trips analysis using Python.

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data =pd.read_csv(r"C:\Users\User\Downloads\uber\uber-raw-data-sep14.csv")
print(data)


# In[8]:


data["Date/Time"] =data["Date/Time"].map(pd.to_datetime)
print(data.head())


# so let’s have a look at each day,weekday and hour to see on which day the Uber trips were highest:

# In[7]:


data["Day"] =data["Date/Time"].apply(lambda x :x.day)
data["Weekday"] =data["Date/Time"].apply(lambda x :x.weekday())
data["Hour"] =data["Date/Time"].apply(lambda x :x.hour)
print(data.head())


# In[10]:


sns.set(rc ={'figure.figsize':(12,10)})
sns.distplot(data["Day"])


# In[11]:


sns.distplot(data["Hour"])


# In[12]:


sns.distplot(data["Weekday"])


# As we are having the data about longitude and latitude so we can also plot the density of Uber trips according to the regions of the New Your city:

# In[17]:


data.plot(kind ='scatter',x="Lon",y='Lat',alpha=0.4,s=data['Day'],label='Uber Tribs', 
         figsize=(12,5),cmap =plt.get_cmap('jet'))
plt.title("uber tripe Analysis")
plt.legend()
plt.show()


# In[20]:


# correlation of weekday and hour
df =data.groupby(['Weekday','Hour']).apply(lambda x:len(x))
df =df.unstack()
sns.heatmap(df,annot =False)


# In[ ]:




