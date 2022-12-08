#!/usr/bin/env python
# coding: utf-8

# In[18]:



import re
result = re.match(r'AV', 'Analytics AV Vidhya')
print(result)#only at the start

result = re.search(r'AV', 'Analytics AV Vidhya')
print(result.group())#only one occurence,any position

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)#list of all the occurences


# In[23]:



# multiline string
string = 'abc 12\de 23n f456'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = '0'
new_string = re.sub(pattern, replace, string) 
print(new_string)


# multiline string
string = 'abc 12\de 23n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = '0'
new_string = re.subn(pattern, replace, string) 
print(new_string)


# In[30]:


import re

string = '39801 356, 2102 1111'
#(1st word)space(2nd word)
# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

print(match)
if match:
  print(match.group())
else:
  print("pattern not found")

print(match.start())
print(match.end())
print(match.span())


# In[56]:


import re

string = 'aaalysstt'
#(1st word)space(2nd word)
# Three digit number followed by space followed by two digit number
pattern = 'a...s'
pattern1 = '^a...s$'

# match variable contains a Match object.
match = re.search(pattern, string) 
print(match.group())


# In[45]:


import re

string = input()
#(1st word)space(2nd word)
# Three digit number followed by space followed by two digit number
pattern = '[abc]'#[a-z]

# match variable contains a Match object.
match = re.findall(pattern, string) 
print(match)


# In[52]:


import re

string = input()
#(1st word)space(2nd word)
# Three digit number followed by space followed by two digit number
pattern = '...'

# match variable contains a Match object.
match = re.findall(pattern, string) 
print(match)


# In[55]:


import re

string = input()
#(1st word)space(2nd word)
# Three digit number followed by space followed by two digit number
pattern = '^In'

# match variable contains a Match object.
match = re.findall(pattern, string) 
print(match)


# In[ ]:




