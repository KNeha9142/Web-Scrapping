#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
from bs4 import BeautifulSoup
import requests
import re


# In[2]:


url="https://www.angelone.in/52-weeks-high-nse"


# In[3]:


page=requests.get(url)
page


# In[4]:


soup=BeautifulSoup(page.text)
soup.prettify


# In[5]:


table=soup.find('table')
table


# In[6]:


table=soup.find('tbody')
table


# In[7]:


rows=table.find_all('tr')
rows


# In[8]:


angel_one=[]
for i in rows:
    cols=i.find_all("td")
    #print(cols)
    stock_sales=[P.text for P in cols]
    #print(car_sales)
    angel_one.append(stock_sales)
print(angel_one)


# In[9]:


Company=[]
LTP=[]
Day_Range=[]
Fifty_Two_Weeks_High=[]

for i in angel_one:
        Company.append(i[0])
        LTP.append(i[1])
        Day_Range.append(i[2])
        Fifty_Two_Weeks_High.append(i[3])


# In[10]:


Company


# In[11]:


LTP


# In[12]:


Day_Range


# In[13]:


Fifty_Two_Weeks_High


# In[14]:


data={'Company':Company,'LTP':LTP,'Day_Range':Day_Range,'Fifty_Two_Weeks_High':Fifty_Two_Weeks_High}


# In[15]:


data


# In[16]:


import pandas as pd


# In[17]:


angel_one=pd.DataFrame(data)


# In[18]:


angel_one


# In[19]:


angel_one.to_csv("52WeekHighNSESTocks-.csv")


# In[ ]:




