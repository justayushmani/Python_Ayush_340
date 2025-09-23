#tuple
mytuple=("apple","banana","cherry","kewi","grapes","melon")
print(mytuple)

#length of tuple
print(len(mytuple))

#tuple constructor
t=tuple(("apple","banana","cherry"))
print(t)

#indexing in tuple
print(mytuple[2])
print(mytuple[-1])
print(mytuple[0:2])
print(mytuple[2:])
print(mytuple[:2])
print(mytuple[-4:-1])

#check if item in tuple

if "apple" in mytuple:
    print("yes")

#inserting element im tuple
t=("ram","shyam","suraj","rajat","ramu")
k=list(t)
k[1]="seeema"
y=tuple(k)
print(k)

#deleting item in tuple
t=("ram","shyam","suraj","rajat","ramu")
k=list(t)
k.remove("shyam")
y=tuple(k)
print(k)

#unpacking of tuple
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)


#using asterisk
fruits=("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
