#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1
import re
p=r'^[A-Z]_[a-z]+'
s=input()
a=re.findall(p,s)
print(a)


# In[5]:


#Q2
import re
p=r'a.b$'
s=input()
a=re.findall(p,s)
print(a)


# In[8]:


import re
p=r'^\w+'
s=input()
a=re.findall(p,s)
print(a)


# In[11]:


import re
p=r'\w+[!?.]$'
s=input()
a=re.findall(p,s)
print(a)


# In[15]:


import re
p=r'\w*z\w*'
s=input()
a=re.findall(p,s)
print(a)

#*-- 0 or more-- Quantity==0  n+1
#+-- 1 or more--range of n 
#?--0 or 1


# In[16]:


import re
p='\Bz\B'
s=input()
a=re.findall(p,s)
print(a)


# In[17]:


#dd-mm-yyyy

import re
p=r'(\d{2})-(\d{2})-(\d{4})'
s=input()
a=re.findall(p,s)
print(a)


# In[20]:


#dd-mm-yyyy

import re
p=r'^\w+$'
s=input()
a=re.findall(p,s)
print(a)


# In[25]:


#dd-mm-yyyy

import re
p=r'^5.*'
s=input()
a=re.findall(p,s)
print(a)


# In[27]:


#dd-mm-yyyy

import re
p=r'.*[0-9]+$'
s=input()
a=re.findall(p,s)
print(a)


# In[30]:


#dd-mm-yyyy

import re
p=r'\d{1,3}'
s=input()
a=re.findall(p,s)
print(a)


# In[31]:


import re
street = '21 Ramkrishna Road'
print(re.sub('Road$', 'Rd.', street))


# In[41]:




import re
p=r'(P.*) (P.*)'
s=input()
a=re.findall(p,s)
print(a)


# In[44]:




import re
p=r'[0-9]+'
s=input()
a=re.findall(p,s)
print(a)


# In[47]:




import re
p=r'\b[a,e]\w*'
s=input()
a=re.findall(p,s)
print(a)


# looking out for words  starting or ending at x-- use \b


# In[49]:


import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", "$", text))


# In[50]:




import re
p=r'\b\w{5}\b'
s=input()
a=re.findall(p,s)
print(a)


# looking out for words  starting or ending at x-- use \b


# In[52]:




import re
p=r'(\b\w{3,5}\b)'
s=input()
a=re.findall(p,s)
print(a)


# looking out for words  starting or ending at x-- use \b


# In[53]:




import re
p=r'(\b\w{4,}\b)'
s=input()
a=re.findall(p,s)
print(a)


# looking out for words  starting or ending at x-- use \b


# In[54]:


import re
text = 'Python Exercises, PHP exercises.'
print(re.sub(" +", "", text))


# In[59]:


import re
p=r'"(.*)"'
s=input()
a=re.findall(p,s)
print(a)


# In[ ]:




