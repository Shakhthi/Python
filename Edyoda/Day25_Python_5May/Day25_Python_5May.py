#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Lambda

def sumxy(x,y):
    
    return x+y

print(sum(5,5))


su=lambda x,y:x+y

print(su(8,8))


#filter

def ef(x):
    
    if x%2==0:
        return False
    else:
        return True

l=[2,3,4,5,6,7,8]    
    
a=tuple(filter(ef,l))
#map and filter ----convert into list,tuple

print(a)


# In[7]:


#Sample Questions
#Q2
dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1
sum = 0
for k in dictionary:
	sum += dictionary[k]
print (sum)


# In[8]:


#Q3
dictionary = {1:'1', 2:'2', 3:'3'}
del dictionary[1]
dictionary[1] = '10'
del dictionary[2]
print (len(dictionary))


# In[9]:


#6
nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']


pos = nameList.index("TTT")
#index vs find--positive -- same value
#--negative---index==error and find==-1

print(pos * 5)


# In[10]:


#Q9

def addToList(listcontainer):
	listcontainer += [10]

mylistContainer = [10, 20, 30, 40]
addToList(mylistContainer)
print(len(mylistContainer))

#list concatenation and append is same
# + and ;.append(3)
#extend
#l1=[0,1] l2=[3,4]
#l3=l1+l2==[0,1,3,4]


# In[11]:


#Q10
values = [1, 2, 3, 4]
numbers = set(values)
def checknums(num):
	if num in numbers:
		return True
	else:
		return False
for i in filter(checknums, values):
	print (i)


# In[12]:


#Q11

L1 = []
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])
print(L1[0][1][1] + L1[2])


# In[13]:


#Q13

print(['love', 'python'][bool('A')])


# In[14]:


#Q14
sets = {3, 4, 5}
sets.update([1, 2, 3])
print(sets)


# In[15]:


#Q15
set1 = {1, 2, 3}
set2 = set1.copy()
set2.add(4)
print(set1)


# In[16]:


#Q17
import string
Line1 = "And Then There Were None"
Line2 = "Famous In Love"
Line3 = "Famous Were The Kol And Klaus"
Line4 = Line1 + Line2 + Line3
print("And" in Line4)


# In[17]:


#Q19

tuples = {}
tuples[(1,2,4)] = 8
tuples[(4,2,1)] = 10
tuples[(1,2)] = 12
_sum = 0
for k in tuples:
    _sum += tuples[k]
print(len(tuples) + _sum)


# In[18]:


#Q20

tuple = (1, 2, 3)
print(2 * tuple)


# In[19]:


#Q22

list1 = [1, 2, 3, 4, 5]
list2 = list1

list2[0] = 0

print(list1) #statement 2


# In[20]:


#Q23


mylist =[0, 5, 2, 0, 'gfg', '', []]
print(list(filter(bool, mylist)))


# In[21]:


#Q27

L = list('123456')
L[0] = L[5] = 0
L[3] = L[-2]
print(L)


# In[22]:


#Q29
d1 = [10, 20, 30, 40, 50]
d2 = [1, 2, 3, 4, 5]
print(d2 - d1)


# In[27]:


#Q30
list = ['a', 'b', 'c']*-5
print(list)


# In[28]:


#Q33
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)


# In[29]:


#Q38

L = [1, 3, 5, 7, 9]
print(L.pop(-3), end = '  ')
print(L.remove(L[0]), end = '  ')
print(L)


# In[30]:


#Q39

my_string = 'TCS'
for i in range(len(my_string)):
	print (my_string)
	my_string = 'a'


# In[ ]:




