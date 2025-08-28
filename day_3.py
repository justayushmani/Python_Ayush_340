# numeric data type

var1=1
var2=True
var3=10.023
var4=10+3j

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

print(id(var1))
print(id(var2))
print(id(var3))
print(id(var4))


# String data type

#multiline string
a="""jgasjgasvdjhavd 
dbjasvdhjdhjad
anmdvjhadvhkDB"""

K='''JAHVDJGASVDJHASD
ASKJDHVBJHASVDHJA'''


#Single line string
b="vahscSDAHGDAH"


#STRING LENGTH
print(len(a))

print(a[4])


#CHECK STRING
txt="hi i am just building and python program"
print("i" in txt)
print("i" not in txt)

print("rajat" in txt)


# SLICING STRING

b= "hello world"
print(b[2:])
print(b[:3])
print(b[0:5])
print(b[-4:-2])



#MODIFY STRING

a="heLLo"
print(a.upper())
print(a.lower())


#REMOVE WHITESPACES

a="   hello world    "
print(a)
print(a.strip())