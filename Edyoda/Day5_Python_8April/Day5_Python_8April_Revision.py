#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Doubt 1

n=int(input())
root=n**0.5

print(int(root))


# In[7]:


#Doubt 2

d = {'a':2,'b':3}
print(d)
 
t = (d,3,'H',9,[9,8])
print(t)
print(type(t[0]))
t[-1][1]=2 
t[0]["a"] = 7
print(t)
print(type(t))

#tuple is immutable but contents(Set,dictonary and list) of the tuple can be anything
t[1]="Ed"
print(t)


# In[ ]:


item1="bread"
item2="pasta"
item3="colgate"
item4="mirch"
items=["bread","pasta","colgate","mirch"]
print(items)
if
item[0]=chips #replace
item.append("butter"


# In[ ]:


toppings = ['hamburger', 'pepperoni', 'mushroom', 'jalepeño', 'cheese', 'bacon']
print(toppings[2:4])


# In[12]:


print("India","USA",end="--",sep="**")
print("China")


# In[ ]:


#saksham Question


# In[16]:


#Datatypes
#int

#example-1,4,78,-3
#string example--"INDIA"
#example of float-5.6,7.6
#example of complex numbers===2+3j
#example list---heterogenous===[3,"IND","Google",6.7]==mutable
#example tuple----hete===immutable==>a=(3,5.6,"India")
#example dict---key value pairs=={"Name":"Edyoda","COst":xxxxxx}
#Set example===no repe,no particular order===(2,3,4,5)==>c=set(3,4,5,6)
#Boolean example only 2 vlaues====True and False


#everything data in python is object===object==>having attributes and methods
#and every datatype is a class
#Default DataType of the input function==values from user(us)==String
#cannot add string with int or float 

a=input("Enter your name")
print(a)

#conversion from one datatype to another datatype
a=int(input("Enter your age"))
print(a)
print(type(a))
print(a+2)

a=float(input("Enter your weight"))

print(a)
print(type(a))

#account --class and customer--object
#string----->' ' or " " or ''' '''


#split and join

#create a list so take the values from the user



# In[17]:


a=input()

b=a.split(",")
#split only with String datatype
print(b)


# In[19]:


a=int(input("Enter a number:- "))

print(float(a))
#integer-5,6
#float-5.55


# In[20]:


a=input("A Enters")
b=input("B Enters")

print(a,b)


# In[26]:


l=["Ed","Yoda","Classroom"]
   
a="".join(l)
   
print(a)   
print(type(a))
print(type(l))   


# In[28]:


#write a program, to take and store numbers in a list from the string input along with addition of all
#numbers

a=input()

b=a.split(",")
sumi=0
for i in b:
    sumi=sumi+int(i)    
print(sumi)    


# In[33]:


#range---->generate a seq of int numbers 
print(range(1,5))#return numbers one by one always....
print([2,3])#print all at once
for i in range(1,5):
    print(i,sep=" ")


# In[47]:


'''
for i in range(1,5):
    print(i,sep=" ")
'''    
#never have decimal or 0 in step
#never have decimal in start or stop

#for i in range(1,5,7):
 #   print(i)
    
for i in range(1,5,-3):
    print(i)    

#for i in range(-1,-8,-3):
 #   print(i,end=" ")      
    

for i in range(-1,-8,-9):
    print(i,end=" ")   


# In[56]:


#variable assignment

a=9
b=a
print(id(a))
print(id(b))
a=8
print(id(a))
a,b,c=45,6,8
print(a,b,c)#fine
#a,b,c=6,7
print(a,b)#error-->variables>values
a1=(45,6) # be default 
a2=45,6#a1 and a2 are same # variable <values except the variable is 1
print(a2)
print(type(a2))
p,q=3,4,5# variable <values except the variable is 1-->Error
print(p)
print(q)


# In[57]:


a=[]
print(id(a))
a=[]
print(id(a))


# In[58]:


counter=100
print(id(counter))
counter=200
print(id(counter))


# In[59]:


l=[2,3,4,5,8]
print(id(l))
l[1]="EdYoda"
print(id(l))


# In[ ]:



a=100
b=6
print(a+b)
print(a-b)
print(a*b)
print(b-a)
print(a/b)#float division ==always decimal
print(a//b)#floor division==always integer
print(a%b)
print(b/a)
print(a**b)

#1.5---floor--1
#1.9--floor--1
#2.0002---floor--2
#leats integer equal or lesser than the float num


# In[60]:



a=9
b=9
print(a>b)
print(a>=b)
print(a<=b)
print(a<b)
print(a!=b)
print(a==b)


# In[61]:



a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(not b)


# In[ ]:


a = 10
# Assign value
b = a
print(b)
# Add and assign value
b += a
#b=b+a
#10+10
print(b)
# Subtract and assign value
b -= a
#b=b-a
#20-10
print(b)
# multiply and assign
b *= a
#b=b*a
#10*10
print(b)
b=b/a
print(b)

#sum=sum+int(i)
#sum+=int(i)


# In[62]:


l=[9,8,7]

print(9 in l)
print(2 not in l)

d={2:"Sagar",3:"EdYoda"}
print(2 in d)
print("Sagar" in d)


# In[63]:


a= True 
b="True"
print( a and b) 


# In[65]:


#is vs ==
a=9
b=8
b=a
print(a==b)
print(a is b)


# In[66]:


a=9
b=9
print(a==b)
print(a is b)


# In[67]:


a=[]

b=[]
print(a==b)
print(a is b)


# In[70]:


a= True
b="true"
s=a and b
print(s)


# In[71]:


a=b   
a=3    
b=5      
print (a==b) 


# In[ ]:




