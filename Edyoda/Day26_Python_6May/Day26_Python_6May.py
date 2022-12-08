#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q40
i = 1
while True:
    if i % 3 == 0:
        break
    print(i)
    i + = 1


# In[3]:


#Q41


T1 = (1)
T2 = (3, 4)
T1 += 5
print(T1)
print(T1 + T2)


# In[4]:


#Q42

D = {1 : 1, 2 : '2', '1' : 2, '2' : 3}
D['1'] = 2
print(D[D[D[str(D[1])]]])


# In[5]:


#Q43

D = {1 : [1, 2, 3], 2: (4, 6, 8)}
D[1].append(4)
print(D[1], end = " ")
L = [D[2]]
L.append(10)
D[2] = tuple(L)
print(D[2])


# In[6]:


#Q46


data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x%2==0]
print(temp)


# In[10]:


#local-function,modules
#global-- uniform accross all the scopes

s="Ed"
def f():
	#print(s)
	# local variable
	s = "I love Geeksforgeeks"
	print(s)

# Driver code
f()
print(s)


# In[17]:


s="Ed"
def f():
	#print(s)
    global s
    print(s)
	    
    
# Driver code
f()
print(s)


# In[20]:


t="Ed"
def f():    
    print(t) 
    
# Driver code
f()
print(t)


# In[21]:


g=1234

def t():
    print(g)
    
t()
print(g)


# In[22]:


g=1234

def t():
    g=455
    print(g)
    
t()
print(g)


# In[33]:


#nested list and nested lambda expression

#l=[output sequence condition(opt)]
#[1,2,3,4]
#list compre
#range
temp="ABC2345"

data = [x for x in (x for x in temp)]
print(data)

a=lambda x:x.upper()
b=lambda y:y.lower()
c=lambda x,y:x+y


d=lambda x:b(x) if (x.isupper()) else a(x)

print(d("X"))

te="ABCxyz"===[a,b,c,X,Y,Z]

#call d() in every element in te==[a,b,c,X,Y,Z]
data = [x for x in (x for x in te if d(x).isupper()) ]

te-ABCxyz

A--d()--a--isupper()-False
B--False
C--False
x--d()--X--isupper()-True
y
z


print(data)


# In[36]:


#D={}

#update --merge two dictionary

#add--one pair at a time

#del components
#clear the dictionary

#d={{3:4},4:6}XXXXX

#d={{3}:4,4:6}XXXX


d={(4,5):4,4:6}

print(d)

for i,y in d.items():
    print(i,y)
    
for i in d.keys():
    print(i)
    
for i in d.values():
    print(i)


# In[38]:


#Keys---Only tuple, integer,string
#values --any datatype

d=lambda x:x**0.5

data = {x:d(x) for x in (1,2,3,4,5) }

print(data)


# In[42]:


def set_list(list):
	list = ["A", "B", "C"]
    
	return list

def add(list):
	list.append("D")
	return list

my_list = ["E"]
print(id(my_list))

a=set_list(my_list)
print(id(a))

c=add(my_list)
print(id(c))


# In[49]:


s={2,3,4,5,4}

#Universal=Real+imaginary

t={2,3}
u={9,0}

print(s)
print(t.union(u))
print(t.intersection(s))



print(t.difference(u))


# In[ ]:




