#!/usr/bin/env python
# coding: utf-8

# In[3]:


class A():
  def d(self):
    print("This is A")

class B(A):
  def d(self):
    print("this is B")

class C(A):
  def d(self):
    print("this is C")
    
a1=A()

a1.d()


# In[6]:


# Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC,abstractmethod

class Animal(ABC):
	@abstractmethod
	def move(self):
		pass
class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")

#c=Animal()
b=Human()
b.move()


# In[9]:


class A():
 pass
class B(A):
 pass
class C(A):
 pass
class D(B,C):
 pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())


# In[12]:


class A():
 pass
class B():
 pass
class C():
 pass
class X(A,B):
 pass
class Y(B,C):
 pass
class P(X,Y,C):
 pass

print(P.mro())
print(X.mro())
print(Y.mro())


# In[ ]:


print(X.mro())

