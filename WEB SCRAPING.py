#!/usr/bin/env python
# coding: utf-8

# # BeatifulSoup web scraping
# 

# In[1]:


from bs4 import BeautifulSoup 
import requests


# In[2]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[3]:


page = requests.get(url)


# In[7]:


BeautifulSoup(page.text, "html")


# In[11]:


soup = BeautifulSoup(page.text, "html")
print(soup.prettify())


# # FIND AND FIND ALL

# In[12]:


from bs4 import BeautifulSoup
import requests


# In[13]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[15]:


page = requests.get(url)


# In[16]:


soup = BeautifulSoup(page.text, "html")


# In[17]:


print(soup)


# In[18]:


soup.find("div")


# In[22]:


soup.find_all("div", class_="col-md-12")


# In[26]:


soup.find_all("p", class_ = "lead")


# In[29]:


soup.find("p", class_ = "lead").text


# In[30]:


soup.find_all("th")


# In[34]:


soup.find("th").text.strip()


# # scraping + PANDA
# 

# In[4]:


from bs4 import BeautifulSoup 
import requests


# In[5]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[6]:


requests.get(url)



# In[7]:


page = requests.get(url)


# In[9]:


BeautifulSoup(page.text, "html")
soup = BeautifulSoup(page.text, "html")


# In[10]:


print(soup)


# In[12]:


soup.find_all("table")[1]


# In[13]:


soup.find("table", class_ = "wikitable sortable")


# In[14]:


table = soup.find_all("table")[1]


# In[15]:


print(table)


# In[24]:


soup.find_all("th")


# In[36]:


world_titles = table.find_all("th")

print(world_titles)


# In[37]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[39]:


import pandas as pd


# In[40]:


df = pd.DataFrame(columns = world_table_titles)


# In[42]:


df


# In[44]:


table.find_all("tr")


# In[47]:


column_data = table.find_all("tr")


# In[54]:


for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[55]:


df


# In[58]:


df.to_csv(r"C:\Users\Chioma\Documents\New folder\companies.csv", index = False)


# In[ ]:




