#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	def __init__(self):
		self.x = 0
class Derived_Test(Test):
	def __init__(self):
		self.y = 1
        #super.__init__()
def main():
	b = Derived_Test()
	print(b.x,b.y)
main()


# In[2]:


class Demo:
	def __init__(self):
		self.x = 1
	def change(self):
		self.x = 10
class Demo_derived(Demo):
	def change(self):
		self.x=self.x+1
		return self.x
def main():
	obj = Demo_derived()
	print(obj.change())
main()


# In[3]:


class class1:
	def __init__():
		print("class1's __init__")
class class2(class1):
	def __init__():
		print("class2's __init__")
ob=class2()


# In[4]:


class test:
	def __init__(self):
		print("Hello World")
	def __init__(self):
		print ("Bye World")
obj=test()


# In[5]:


int = 1
def randommethod():
	global int
	for i in (1, 2, 3):
		int += 1
randommethod()
print(int)


# In[6]:


class class1:
	def __init__(me,a):
		me.a=a
		print(a)
ob=class1(10)


# In[ ]:




