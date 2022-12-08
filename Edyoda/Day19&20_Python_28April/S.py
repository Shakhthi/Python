# a file named "geek", will be opened with the reading mode.
#file = open('IPI.txt', 'w')
# This will print every line one by one in the file

#file.write("This is the ISL Page information")

#print(file.read(10))

#print(file.read(10))

#print(file.readline(500))


#a=file.readlines()

#print(a)
#for i in file:
#    print(i.readline())


#for i in range(2,7):
 #   print(a[i])

#l=["This is Sagar ","This is Edyoda"]
#file.writelines(l)    


# Python program to illustrate
# Append vs write mode



# Append-adds at last
file1 = open("python.txt", "a") # append mode
file1.write("\n This is the new line \n")
file1.close()

with open("IPI.txt", 'a') as file1:
    file1.write("Today")




