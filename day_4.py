#REPLACE A STRING
a="hello world"
print(a.replace("h","j"))


# SPLIT STRING
a="hello world"
print(a.split(" "))

# CONCATENATE STRING
a="hello"
b="world"
print(a+" "+b)

#FORMAT STRING
age=36
txt=f"My name is John, and I am {age}"
print(txt)


# BOLLEAN DATA TYPE
print(10<9)
print(bool("Abc"))
print(bool(0))
print(bool(1))
print(bool(123))

#FUNCTIONS CAN RETURN BOOLEAN
def myFunction() :
    return False     
print(myFunction())

#sequence data type

#list
thislist = ["apple", 8 , "cherry"]
newlist = ["x","y","z"]
print(thislist)
print(thislist[1])  #print index 1
print(thislist[-1])  #print last index
print(thislist[1:3])  #print index 1 to 2
print(thislist[:2])  #print index 0 to 1
print(thislist[1:])  #print index 1 to end
print(thislist * 2)  #print list two times
print(thislist + newlist)  #concatenate two lists
print(type(thislist)) #data type of thislist


#tuple
thistuple = ("apple", 8 , "cherry")
newtuple = ("x","y","z")
print(thistuple)
print(thistuple[1])  #print index 1
print(thistuple[-1])  #print last index
print(thistuple[1:3])  #print index 1 to 2
print(thistuple[:2])  #print index 0 to 1
print(thistuple[1:])  #print index 1 to end
print(thistuple * 2)  #print tuple two times
print(thistuple + newtuple)  #concatenate two tuples
print(type(thistuple)) #data type of thistuple

#range
for i in range(10):  #0 to 9
  print(i)


for i in range(1,10,2):  #start,stop,step
  print(i)

