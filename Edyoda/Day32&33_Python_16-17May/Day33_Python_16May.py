#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
import pytest
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 49
    
test_sqrt()  
testsquare()


# In[5]:


# A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))


# In[6]:


# A Python program to demonstrate update()
from collections import Counter
coun = Counter()

coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)

coun.update([1, 2, 4])
print(coun)


# In[7]:


# An example program where different list items are
# counted using counter
from collections import Counter

# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

# Count distinct elements and print Counter aobject
print(Counter(z))


# In[8]:


# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for i,j in d.items():
    
    print(i,j)
    


# In[10]:


# Python code to demonstrate working of
# append(), appendleft(), pop(), and popleft()

# importing "collections" for deque operations
import collections

# initializing deque
#list
de = collections.deque([1,2,3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(9)
print(de)

# printing modified deque
print ("The deque after appending at right is : ")
print (de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(23)

# printing modified deque
print ("The deque after appending at left is : ")
print (de)

# using pop() to delete element from right end
# deletes 9 from the right end of deque
de.pop()

# printing modified deque
print ("The deque after deleting from right is : ")
print (de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print ("The deque after deleting from left is : ")
print (de)


# In[20]:


# Python program to demonstrate
# userdict


from collections import UserDict


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):
	
	# Function to stop deletion
	# from dictionary
	def __del__(self):
		raise RuntimeError("Deletion not allowed")
		
	# Function to stop pop from
	# dictionary
	def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")
		
	# Function to stop popitem
	# from Dictionary
	def popitem(self, s = None):
		raise RuntimeError("Deletion not allowed")
	
# Driver's code
d = MyDict({'a':1,
	'b': 2,
	'c': 3})

print("Original Dictionary")
print(d)

d.pop(1)


# In[21]:


# Python program to demonstrate
# userlist


from collections import UserList


# Creating a List where
# deletion is not allowed
class MyList(UserList):
	
	# Function to stop deletion
	# from List
	def remove(self, s = None):
		raise RuntimeError("Deletion not allowed")
		
	# Function to stop pop from
	# List
	def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")
	
# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
L.remove()


# In[23]:


# Python program to demonstrate
# userstring


from collections import UserString


# Creating a Mutable String
class Mystring(UserString):
	
	# Function to append to
	# string
	def append(self, s):
		self.data += s
		
	# Function to remove from
	# string

	
# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)


# In[24]:



import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)


# In[25]:


import datetime

date_object = datetime.date.today()
print(date_object)


# In[26]:


import datetime
#date is a class of module datetime
#every class has a constructor
d = datetime.date(2019, 4, 13)
print(d)


# In[27]:


from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# In[31]:



from datetime import datetime, date

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t5 - t4
print("t6 =", t6)
print(type(t6))


# In[32]:


from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))


# In[35]:


from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M")
print(t)


# In[37]:



from datetime import datetime

s1 = now.strftime("%d/%m/%Y, %H:%M:%S")

#time to string
print(s1)


# In[41]:


#string to time

from datetime import datetime

date_string = "21-October-2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d-%B-%Y")
print("date_object =", date_object)


# In[ ]:




