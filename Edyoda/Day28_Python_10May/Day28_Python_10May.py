#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Aadhar:
    org="UIDI"
    
#CONSTRUCTOR HELPS YOU TO INITIALIZE VALUES TO YOUR OBJECTS
#__init__   
    def __init__(self,ano,name,address):
        self.ano=ano
        self.name=name
        self.address=address        
a1=Aadhar(123,"Sagar","Noida")
#self--reference word not a  keyword--so you can change it
print(a1.ano)
print(a1.name)
print(a1.address)
print(a1.org)
a2=Aadhar(113,"Preeti","Noida") 
print(a2.ano)
print(a2.name)
print(a2.address)
print(a2.org)
print(a2)


# In[10]:


class EdYoda:
    cName="MLDS"
    
    def __init__(self,sName,sID,sMark):
        self.sName=sName
        self.sID=sID
        self.sMark=sMark
        
    def __init__(self):
        print("Def constr called")
        
    def pme(self):
        print(self.cName)
    
#default constr

S1=EdYoda()
print(S1.cName)
S1.pme()
#S2=EdYoda("Shreya",123,90)
#print(S2.sName)    


# In[15]:


#inheritence
#inheriting properties and beha from parent

#single

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")
        
O=Child()
O.func1()
O.func2()
T=Parent()
#T.func2()
T.func1()


# In[21]:


#Multiple Inheritence

# Python program to demonstrate
# multiple inheritance
# Base class1
class Mother:
	mothername = "Mothr"
	def mother(self):
		print(self.mothername)
# Base class2
class Father:
	fathername = "Father"
	def father(self):
		print(self.fathername)
# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)        
P=Son()
P.parents()
Q=Father()
#Q.parents()
Q.father()
R=Mother()
#R.parents()
R.mother()


# In[30]:


# Base class
class Grandfather:
    grandfathername="OOOO"

# Intermediate class
class Father(Grandfather):
    fathername="PPPPPPP"


# Derived class
class Son(Father):
	def __init__(self,sonname):
		self.sonname = sonname
        
	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)
        
        
P=Father() 

R=Son("RRRRR")
R.sonname
R.print_name()


# In[34]:


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")
P=Child2()
#P.func2()
P.func1()
Q=Child1()
Q.func2()
Q.func1()



# In[35]:


#Polymorphism

#Polymorphism and Method Overriding---comes from Multiple Inheritence

#polymorphism --one method diff behaviours

#len()

l=[3,4,5,6]
t=(3,4)
s="7879"
print(len(t))
print(len(l))
print(len(s))


# In[45]:


#Method Overriding 

#when you try to redefine a method with same name but diff implementation

# Defining parent class
class Parent:
	
	# Constructor
	def __init__(self):
		self.value = "Inside Parent"		
	# Parent's show method
	def show(self):
		print("Parent class implementation")		
# Defining child class
class Child(Parent):	
	# Constructor
	def __init__(self):
		self.value = "Inside Child"		
	# Child's show method
	def show(self):
		print("Child Class imple")        
P=Child()
P.show()
Q=Parent()
Q.shown()

        


# In[46]:


# Defining parent class 1
class Parent1():
		
	# Parent's show method
	def show(self):
		print("Inside Parent1")
		
# Defining Parent class 2
class Parent2():
		
	# Parent's show method
	def display(self):
		print("Inside Parent2")
		
		
# Defining child class
class Child(Parent1, Parent2):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
		
# Driver's code
obj = Child()

obj.show()
obj.display()


# In[51]:


class Parent():
	
	def show(self):
		print("Inside Parent")
		
class Child(Parent):
	
	def show(self):
		
		# Calling the parent's class
		# method
		Parent.show(self)
		print("Inside Child")
		
# Driver's code
obj = Child()
obj.show()
P=Parent()
P.show()


# In[ ]:




