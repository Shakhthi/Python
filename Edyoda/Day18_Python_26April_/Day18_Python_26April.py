#!/usr/bin/env python
# coding: utf-8

# In[9]:



"""
#function revision
def calculation(x,y=9,z):
  
  q=(x*y)/z
  return q

def stringop(s1,s2):
    
    print(s1+s2)
    
#calculation(10,2,2)
print(calculation(10,2,2))
print(calculation(10,5,2))
print(calculation(10,2,5))#positional argu

print(calculation(10,z=2,y=5))
print(calculation(10,z=2))

"""
def prtoppers(*names):
    
    a=[]
    for n in names:
        a.append(n)
    return a


ans=prtoppers("A","B","C")
ans1=prtoppers("A")
print(ans)
print(ans1)
    
    


# In[14]:


#namespace

# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
    print(x)

# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


# In[ ]:


def myFun(x):

	# After below line link of x with previous
	# object gets broken. A new object is assigned
	# to x.
	x = 20
# Driver Code (Note that lst is not modified
# after function call.
x = 10
myFun(x)
print(x)


# In[15]:


def x():
    global a
    a = 9
    print(a, id(a))


x()
global a
a = 10
print(a, id(a))
x()
print(a, id(a))


# In[16]:


def x():
	global a
	a = 9
	print(a, id(a))

x()
a=10
print(a,id(a))
x()
global a

a=18
print(a)


# In[ ]:




