#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Python program to demonstrate
# use of lambda() function
# with map() function
ani = [3,4,5,6]

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = tuple(map(lambda a: a**0.5, ani))

print(uppered_animals)


# In[9]:


def cube(x):
    
    return x*x*x
#s=x*x*x
#return s
#s=x**3
#pow()
print(cube(3))
#lambda function/anonymous---miniature version-smaller operations-return  atmost 1 value
#cu=lambda A...:B A-input(s),B-Output
cu=lambda x:x**3
ad=lambda x,y,z:x+y+z
print(cu(3))


# In[10]:


# Return double of n
def double(n):
	return n + n

ad=lambda x:x+x

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(double, numbers)
print(list(result))
res = list(map(ad, numbers))
print(res)

m=[30,60]

m=[30*100/80,60*100/80]

#whenver you want to fetch a list from an  old list  by including some modif
#use map..as it poingt sto the elements one by one


# In[13]:


numbers1 = [1, 2, 3]
numbers2 = [4, 5,9]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


# In[14]:


n=int(input())
l=[]
for i in range(n):
   e=int(input())
   l.append(e)    
sq=lambda x:x**2
r=list(map(sq,l))
print(r)


# In[19]:


# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test =tuple(map(tuple, l))
print(test)


# In[23]:


h=lambda x:x**2
l=lambda y:print(y**3)

Max = lambda a, b : h(a) if(a > b) else l(b)

print(Max(1, 2))



# In[24]:


# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# In[25]:


# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))

print(adults)


# In[26]:


# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)


# In[29]:


a=[x.upper() for x in ['a','b'] ]
print(a)


# In[32]:


d={x:chr(x) for x in range(97,123)}
print(d)
#ord--to get ascii value from character
#chr--to get charcter from ascii value
ds={x for x in range(97,123)}
print(ds)
print(type(ds))


# In[33]:


List = [True, 50, 10]  # True,50,5,10
List.insert(2, 5)   
print(List, "Sum is: ", sum(List))


# In[34]:


x = 'abcd'
a=[]
for i in x:
    i.upper()
        
    


# In[ ]:


p = '^[7|8|9]+\d{9}'

