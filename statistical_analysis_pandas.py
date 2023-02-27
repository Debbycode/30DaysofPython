#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np


# In[2]:


nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)


# In[3]:


fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)


# In[4]:


dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)


# In[5]:


s = pd.Series(10, index = [1, 2, 3])
print(s)


# In[6]:


s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)


# In[ ]:





# In[7]:


data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)


# In[8]:


data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)


# In[9]:


data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)


# Reading CSV File Using Pandas

# In[12]:


import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)

# In[13]:


print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method


# In[14]:


print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method


# In[15]:


print(df.shape) # as you can see 10000 rows and three columns


# In[16]:


print(df.columns)


# In[18]:


heights = df['Height'] # this is now a series


# In[19]:


print(heights)


# In[21]:


weights = df['Weight'] # this is now a series
print(weights)


# In[22]:


print(len(heights) == len(weights))


# In[23]:


print(heights.describe()) # give statisical information about height data


# In[24]:


print(weights.describe())


# In[25]:


print(df.describe())  # describe can also give statistical information from a dataFrame


# In[26]:


import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)


# In[27]:


weights = [74, 78, 69]
df['Weight'] = weights
df


# In[28]:


heights = [173, 175, 169]
df['Height'] = heights
print(df)


# In[29]:


df['Height'] = df['Height'] * 0.01
df


# In[30]:


# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()


# In[31]:


df['BMI'] = bmi
df


# In[32]:


df['BMI'] = round(df['BMI'], 1)
print(df)


# In[33]:


birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
df


# In[34]:


print(df.Weight.dtype)


# In[36]:


df['Birth Year'].dtype # it gives string object , we should change this to number


# In[38]:


df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now


# In[39]:


df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype


# In[40]:


ages = df['Current Year'] - df['Birth Year']
ages


# In[41]:


df['Ages'] = ages
print(df)


# In[42]:


mean = (35 + 30)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what


# Boolean Indexing

# In[46]:


print(df[df['Ages'] > 120])


# In[47]:


print(df[df['Ages'] < 120])


# In[50]:


my_data= pd.read_csv('hacker_news.csv')


# In[51]:


my_data.head()


# In[55]:


my_data.tail()


# In[70]:



title_series = my_data['title']
print(title_series)


# In[73]:


num_rows = my_data.shape[0]
num_columns = my_data.shape[1]

print (num_rows)
print (num_rows)


# In[74]:


my_data.shape


# In[75]:


python_titles = my_data[my_data['title'].str.contains('python', case=False)]
print(python_titles)


# In[76]:


javascript_titles = my_data[my_data['title'].str.contains('javascript', case=False)]
print(javascript_titles)


# In[ ]:




