#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
import bs4
url='https://en.wikipedia.org/wiki/Rajasthan_Royals'

data=requests.get(url)#gets all the data about the page
#view-source:https://www.youtube.com/user/ImagineDragons/videos
#print(data.text)

a=bs4.BeautifulSoup(data.text,'html.parser')
#print(a.prettify())# gives you the HTML code

#for example you want to print for a tag
#tagsss
for para in a.find('h1'):#finds only the first
    pass
   # print(para)
    
for para in a.find_all('h3'):#find every
    pass 
    #print(para)    #with tag
    
for para in a.find_all('h3'):#find every
    pass
   # print(para.text)   #without tag 
    
for links in a.find_all('a'):#to find all the links
    link=links.get('href')
    
    print(link)#with random text
    
#for para in soup.find_all('a'):
  #  link = para.get("href")
   # if link[0:6] =="/wiki/" and link!="#":
     #   pass
       # print("https://en.wikipedia.org/"+link)
  #  elif link[0]=="/" and link!="#":
     #   pass
        #print("https://en.wikipedia.org/"+link)
   # elif link!="#":
   #     pass
       # print(link)


# In[14]:


import json

with open('tt.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)


# In[10]:


#extract Image links

import requests
from bs4 import BeautifulSoup
	
def getdata(url):
	r = requests.get(url)
	return r.text
	
htmldata = getdata("https://en.wikipedia.org/wiki/Virat_Kohli")
soup = BeautifulSoup(htmldata, 'html.parser')
urls=[]
for item in soup.find_all('img'):
	
    s='https://'+item['src']
    urls.append(s) 
    print('https:'+item['src'])
print(urls,len(urls))    


# In[12]:


import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])
print(person_dict['name'])


# In[13]:



import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)


# In[15]:


value = [1, 2, 3, 4]
data = 0
try:
    data = value[3]
except IndexError:
    print('GFG IndexError  ', end = '')
except:
    print('GeeksforGeeks IndexError  ', end = '')
finally:
    print('Geeks IndexError  ', end = '')  
data = 10
try:
    data = data/0
except ZeroDivisionError:
    print('GFG ZeroDivisionError  ', end = '')
finally:
    print('Geeks ZeroDivisionError  ')


# In[17]:


class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
        print(var)
obj=test()
print(obj.variable)


# In[19]:


def procedural(val1): 
    try: 
        sum1=0 
        for item in str(val1):
            sum1+=int(item_val)
    except TypeError:
        print("Type error occurred")
    finally:
        print("Finally in function")
    print("Function executed successfully")
try: 
    procedural(792)
    print("Try handled")
except ValueError:
    print("Value error occurred")
except NameError:
    print("Name error occurred")
finally:
    print("Finally in main")
    
#if internal try excpet not able to handle the excpetion
#then go to the outer try block to handle it--in nested try except block   


# In[ ]:




