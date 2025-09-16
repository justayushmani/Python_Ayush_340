# Break Statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

# Continue Statement
# The continue statement is used to skip the current iteration of a loop and move to the next
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#for  loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in fruits:
 print(x)
print(type(fruits))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in fruits:
 print(x)
 if(x=="cherry"):
    break
 
 #range function
for x in range(10):
 print(x)

#pass statement
for x in [0, 1, 2]:
 pass   
print("Hello")