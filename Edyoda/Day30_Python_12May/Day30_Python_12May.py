#!/usr/bin/env python
# coding: utf-8

# In[1]:


# program to illustrate public access modifier in a class



# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()


# In[42]:


"""
class Geek:
	
	# constructor
	def __init__(self, name, age):
		
		# public data members
		self.__geekName = name
		self.geekAge = age

	# public member function	
	def displayAge(self):
		
		# accessing public data member
		print("Age: ", self.geekAge)
        
    def displayName(self):
        print('Name is ',__geekName)
"""
        
A=Geek("Sagar",25)  

print(A.geekAge)
#print(A.geekName)
A.displayName()


# In[18]:


class Geek:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch):
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function
	def __displayDetails(self):
		
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
			
		# accessing private member function
		self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")
#print(obj.__displayDetails())
print(obj.__name)

# calling public member function of the class
obj.accessPrivateFunction()



# In[21]:


# super class
class Student:
	
	# protected data members
	_name = None
	_roll = None
	_branch = None
	
	# constructor
	def __init__(self, name, roll, branch):
		self._name = name
		self._roll = roll
		self._branch = branch
	
	# protected member function
	def _displayRollAndBranch(self):

		# accessing protected data members
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)
# derived class
class Geek(Student):

	# constructor
	def __init__(self, name, roll, branch):
        #public       
			Student.__init__(self, name, roll, branch)#instead of having own constr it is 
            #calling parent class constructor
		
	# public member function
	def displayDetails(self):
				
				# accessing protected data members of super class
				print("Name: ", self._name)
				
				# accessing protected member functions of super class
				self._displayRollAndBranch()

# creating objects of the derived class	
obj = Geek("R2J", 1706256, "Information Technology")
#print(obj.name)
# calling public member functions of the class
obj.displayDetails()


# In[23]:


class Geek:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch):
		self.__name = name
		self.__roll = roll
		self.__branch = branch
	
	# public member function
	def accessPrivateFunction(self):
			
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)



# creating object
obj = Geek("R2J", 1706256, "Information Technology")
print(obj.__name)
# calling public member function of the class
obj.accessPrivateFunction()


# In[29]:


try:
    a=int(input())
    b=int(input())

    c=a/b
except:
    print("Error caught")
else:    
    print(c)
    print('The End')
    print("TCS")
    
finally:
    print("Atlast")


# In[32]:


try:
    a=int(input())
    b=int(input())

    c=a/b

finally:
    print("Atlast")


# In[33]:


d={2:3}
print(d[6])


# In[34]:


l=[4,5]

print(l[9])


# In[36]:


def x():
    y=y+1

    
y=9
x()
print(y)


# In[38]:


try:
    a=int(input())
    b=int(input())

    c=a/b
    l=[4,5]
    print(l[9])
except ZeroDivisionError:
    print("ZeroDivisionError Error caught")
except IndexError:
    print("IndexError caught")
    
else:    
    print(c)
    print('The End')
    print("TCS")
    
finally:
    print("Atlast")


# In[40]:


try:
    a=int(input())
    b=int(input())

    c=a/b
    l=[4,5]
    print(l[9])
except Exception:
    print(" Error caught")
else:    
    print(c)
    print('The End')
    print("TCS")
    
finally:
    print("Atlast")


# In[41]:


#static method and class method--Both of them are related to class

from datetime import date
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)
	
	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(22))



# In[ ]:


class Geek:
	
	# constructor
	def __init__(self, name, age):
		
		# public data members
		self.geekName = name
		self.geekAge = age

	# public member function	
	def displayAge(self):
		
		# accessing public data member
		print("Age: ", self.geekAge)
        
#Encpsulation- capturing /storing all in one place--methods, constr, attributes

