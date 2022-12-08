#!/usr/bin/env python
# coding: utf-8

# In[7]:


course = "some examples of python program"
#split of the line into list of words
print(course[0])
print(len(course))
a=course.split(" ")
print(a[-1])#last word
print(a[0])#first word
print(len(a))
print(a)


# In[13]:


a=[]
b=input("Enter the values of the list separated by semi colon: ")
a=b.split(" , ")
print(a)


#when you are giving input, only use the decided seperator


# In[6]:


a=[4,5,6,7,8]

print(a[0])#first
print(a[1])#2nd element
print(a[-1])#list last element
print(a[-5])
# 4,5,6,7,8
#forward direction indices-->0,1,2,3,4
#back direction indices-->-5,-4-3,-2,-1


# In[16]:


a=input("enter the roll no.: ")
print(int(a))
lis=a.split(" ")
#split is only for string
print(lis)


# In[19]:


t=(3,4,5,6)
#tuple into list
tuplel=list(t)
print(t)
#t.append(3)
tuplel.append(3)
print(tuplel)
print(tuple(tuplel))


# In[40]:


a=67
print(a)
#python gives id function to know the location of my object--(67)
print(id(a))
a="Sagar"
print(id(a))
b=a
print(id(b))

# one object can be referenced by n no of variables


# In[25]:


l=[3,4,5,6,7]
#normal list
print(id(l))
print(l)
l[1]=9
print(id(l))
print(l)
l.append(10)
print(id(l))
print(l)
# that is why list is mutable


# In[27]:


t=(2,3,4,5)
#as it is not referenced by any variable so picked up automaticaally
#by garbage collector 
print(id(t))

#t[1]=9
t=(6,7,8,9,10)
#invalid as tuple is immutable
print(id(t))


# In[28]:


a=[1,2,3,4,5,6]         
b=[1,2,3,4,5,6]
print(id(a))
print(id(b))


# In[ ]:


a=[1,2,3,4,5,6]         
b=a
print(id(a))
print(id(b))
#example of immutable---tuple,string,int,float,complex
#mutable is list,dictionary and set


# In[31]:


d={"Name":"Sagar","id":23}
print(d)
print(id(d))
d["id"]=90
print(d)
print(id(d))
e=d
print(id(e))
#dictionary is mutable


# In[36]:


d={"Name":"Sagar","id":23}

#name and id are keys
#sagar and 23 are values
#keys are always immutable , mutable not allowed
#values are can be mutable or immutable

#e={"Name":"Sagar","id":23,[2,3,4]:33}

#print(e)
f={"Name":"Sagar","id":23,"Sub":("Maths","chemistry","Biology")}
print(f)


# In[ ]:


#range is nota  datatype--


# In[32]:


s="sagar"

print(id(s))

s="Edyoda"
print(id(s))


# In[37]:


roll=8976
print(id(roll))
roll=9000
print(id(roll))


# In[41]:


f={"Name":"pavi","Sub":(67,56,78)}
print(f)
print(id(f))
f={"Name":"pavi","Sub":(68,56,78)}
print(f)
print(id(f))


# In[42]:


marks = {"english" : 95, "chemistry" : 98}
print (marks)
print (id(marks))
print(marks["chemistry"])
print(id(marks["chemistry"]))
marks["physics"] = 97
print(marks)
print(id(marks))
marks["physics"] = 92
print (marks)
print (id(marks))
#adding keys and values or reassigning into dictionary wont change the address as dictionary is
#mutable


# In[45]:


#arithmetic operations
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
#1.3===floor(1.3)==1
#1.9==floor(1.9)==1

#16*6=96==100-4
#100=16*6+4


# In[ ]:


#all the false values in python
'''
0
[]=empty list
None==it ia keyword
(,)=empty tuple
{}=empty dict
""=empty string
'''
#all other values apart from these is true
#exa=-9.7,2+8j


# In[53]:


if({}):
    print("tt")    
else:
    print("ff")


# In[56]:


a=98
b=34
#== is a comparison operator
#= is a assignment operator
#comparison Operators
#output is only of two types==True and False==boolean
print(a>b)
print(a>=b)
print(a<=b)
print(a<b)
print(a!=b)
print(a==b)


# In[58]:


a=True
b=False
#logical operator
#And means True in both true condition else false
#or means true if either of them is true
#not reverse boolean
print(a and b)
print(a or b)
print(not a)
print(not b)


# In[61]:


#assignment operators
# Examples of Assignment Operators
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


# In[69]:


#Membership operator
# in and not in
l=[4,5,9,67]
# output is  always boolean
print(4 in l)
print(3 in l)
s="EdYoda"
print("Ed" in s)
print("ed" in s)
d={"A":34,"B":45}
# in dictionary membership is always confirmed with the help of keys not values
print("A" in d)
print(34 in d)
print(34 not in d)
 


# In[73]:


#identity operator 
# is and ==

#is refers to the id of the object for comparison
#== refers to the value of the object for comparison
a=9
b=9
#b=a
print(id(b))
print(id(a))

print(a is b)
print(a==b)


# In[75]:


list1 = []
list2 = []
list3=list1

print(id(list1))

print(id(list2))

print(id(list3))

if (list1 == list2):
	print("True")
else:
	print("False")

if (list1 is list2):
	print("True")
else:
	print("False")

if (list1 is list3):
	print("True")
else:
	print("False")
list3 = list3 + list2
# we are doing list reassignment not modification bcoz modificatiion is allowed in list
#that si why diff id
print(id(list3))
if (list1 is list3):
	print("True")
else:
	print("False")


# In[ ]:




