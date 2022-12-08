#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Seq:

   def __init__(self,limit):#start&stopping point
       
      self.x = 0
      self.limit=limit

   def __next__(self):
   
        # Store current value ofx 
        x = self.x 
  
        # Stop iteration if limit is reached 
        if x >= self.limit: #helps you to stop
            raise StopIteration 
 
       # Else increment and return old value 
        
        self.x =self.x+ 1 #step
        return self.x+25      
    
   def __iter__(self):
       
      return self

#s = Seq(6)

for e in Seq(10):

   print(e)

for i in range(1,11):
    print(i*i)
    
    


# In[9]:


def x(y):
 return(y*y)
 print("Hello")# XXXXXXXXXXXXXXXX

print(x(8))

#return never comes back into the func


# In[10]:


def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value) 


# In[16]:


def fib(limit): 
	
	# Initialize first two Fibonacci Numbers 
	a, b = 0, 1

	# One by one yield next Fibonacci Number 
	while a < limit: 
		yield a 
		a, b = b, a + b 
"""
limit-6
a=0,b=1
yield-0
a=1,b=1
yield=1
a=1,b=2
.......

"""
# Create a generator object 
x = fib(5)
print(next(x))
print(next(x))
print(next(x))
print("------")
#this is iterator
for i in fib(6):
    print(i)


# In[17]:


class One:
    def __init__(self, a):
        self.a = a
    def __add__(self, object2):
        return self.a + object2.a
class Two:
    def __init__(self, a):
        self.a = a
    def __add__(self, object2):
        return self.a + object2.a
a_instance = One(10)
b_instance = Two(20)
print(a_instance + b_instance)
# Output: 30


# In[21]:


class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
a = A([1, 2, 3])
print("First item:" ,a[4])


# In[23]:


class LenExample:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)
len_instance = LenExample([1, 2, 3])
b=LenExample((1,2,3,4))
print(len(b))##4

#c=LenExample(3)
#print(len(c))##3 is an integer value

#len works with tuple.string and list !!!!
print(len(len_instance))
# Output: 3


# In[25]:


class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
        return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a
a = Comparison(1)
b = Comparison(2)
print(
    a < b,
    a > b,
    a <= b,
    a >= b,
    a == b,
    a != b
)


# In[ ]:




