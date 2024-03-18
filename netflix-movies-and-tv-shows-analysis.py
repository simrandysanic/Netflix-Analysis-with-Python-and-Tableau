#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install numpy==1.24.1


# In[3]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')


# In[4]:


df = pd.read_csv('netflix_titles.csv')


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.columns.tolist()


# In[8]:


df.duplicated().sum()


# In[9]:


df.isna().sum()


# In[10]:


df.dropna(inplace=True)


# In[11]:


df.info()


# In[12]:


df.drop(columns=['show_id','title', 'cast', 'description'], inplace=True)


# In[13]:


df.rename(columns={'listed_in' : 'category'}, inplace=True)


# In[14]:


df.head()


# In[15]:


df.reset_index(drop=True)


# In[16]:


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', infer_datetime_format=True)


# In[17]:


df.info()


# In[18]:


types =  df['type'].value_counts()
types


# In[38]:


top_10_directors_movie = df['director'][df['type'] == 'Movie'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_directors_movie


# In[34]:


top_10_directors_TVShow = df['director'][df['type'] == 'TV Show'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_directors_TVShow


# In[21]:


top_10_countries_movie = df['country'][df['type'] == 'Movie'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_countries_movie


# In[22]:


top_10_countries_TVShow = df['country'][df['type'] == 'TV Show'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_countries_TVShow


# In[23]:


top_10_rating_movie = df['rating'][df['type'] == 'Movie'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_rating_movie


# In[24]:


top_10_rating_tvshow = df['rating'][df['type'] == 'TV Show'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_rating_tvshow


# In[25]:


top_10_category_moive = df['category'][df['type'] == 'Movie'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_category_moive


# In[26]:


top_10_category_tvshow = df['category'][df['type'] == 'TV Show'].value_counts().sort_values(ascending=False).iloc[0:10].reset_index()
top_10_category_tvshow


# In[27]:


df['date_added_year'] = df['date_added'].dt.year


# In[28]:


df.head()


# In[29]:


date_added =  df['date_added_year'].value_counts()
date_added


# In[65]:


colors = ['#AAD7D9', '#FFE5E5']  

plt.figure(figsize=(10, 6))
plt.pie(types, labels=['Movies', 'TV Shows'], autopct='%1.1f%%', explode=[0, 0.1], colors=colors)
plt.title('Movies & TV Shows')
plt.legend()
plt.show()


# In[63]:


plt.figure(figsize=(10,5))
plt.bar(top_10_directors_movie['index'],top_10_directors_movie['director'], color = "#E6A4B4" , label='Count')
plt.title('Top 10 Movie Directors')
plt.xlabel('Directors')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.yticks(np.arange(0,20,2))
plt.legend()
plt.show()


# In[62]:


plt.figure(figsize=(10,4))
plt.bar(top_10_directors_TVShow['index'],top_10_directors_TVShow['director'], color = "#D37676" , label='Count')
plt.title('Top 10 TV Shows Directors')
plt.xlabel('Directors')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[61]:


plt.figure(figsize=(10,5))
plt.bar(top_10_countries_movie['index'],top_10_countries_movie['country'], color = "#51829B" , label='Count')
plt.title('Top 10 Movie Countries')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[60]:


plt.figure(figsize=(10,5))
plt.bar(top_10_countries_TVShow['index'],top_10_countries_TVShow['country'], color = "#E2BFB3" , label='Count')
plt.title('Top 10 TV Shows Countries')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[59]:


plt.figure(figsize=(10,5))
plt.bar(top_10_category_moive['index'],top_10_category_moive['category'], color = "#8E7AB5" , label='Count')
plt.title('Top 10 Movie Category')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[58]:


plt.figure(figsize=(10,5))
plt.bar(top_10_category_tvshow['index'],top_10_category_tvshow['category'], color = "#B5C0D0" , label='Count')
plt.title('Top 10 TV Shows Category')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[57]:


plt.figure(figsize=(10,5))
plt.bar(top_10_rating_movie['index'],top_10_rating_movie['rating'], color = "#B0C5A4" , label='Count')
plt.title('Top 10 Movie Ratings')
plt.xlabel('Ratings')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[56]:


plt.figure(figsize=(8,5))
plt.bar(top_10_rating_tvshow['index'],top_10_rating_tvshow['rating'], color = "#E1AFD1" , label='Count')
plt.title('Top 5 TV Show Ratings')
plt.xlabel('Ratings')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[55]:


plt.figure(figsize=(8,6))
plt.hist(df['date_added_year'], bins=14, label='Count', color = "#9BB0C1" );
plt.grid(True)
plt.title('Distribution of Date Added Years')
plt.xlabel('Years')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[ ]:




