a=11
b=2
print(a+b)

print(id(a))

print(id(b))

# Camel case
myVariableName=10
print(myVariableName)

# Snake case
my_variable_name=10
print(my_variable_name)

# Pascal case
MyVariableName=10 
print(MyVariableName)

# Many value to multiple variables
x,y,z=10,20,30
print(x,y,z)
print(id(x))
print(id(y))  
print(id(z))



# Unpack a collection
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)    
print(y)
print(z)



# Global variable
x="awesome"
def myfunc():
    print("Python is "+x)
myfunc()