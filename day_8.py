#list creation
list1=["rohan","rajat","ramesh"]
print(list1)
print(type(list1))

#mutable in nature
print(list1[0])
list1[0]="ayush"
print(list1)

#store different types of data
list2=[1,2.5,"hello",True]

#allow duplication
list3=[1,2,3,1,2,3]
print(list3)

#length of list
print(len(list3))

#list constructor
list4=list(("apple","banana","cherry"))
print(list4)

#accessing elements
print(list4[1])
print(list4[-1])

#range of indexes
print(list4[1:3])
print(list4[:3])
print(list4[2:])
print(list4[-3:-1])

#check if item exists
if "apple" in list4:
    print("yes apple is present")

#append function
list4.append("orange")

#extend function
list4.extend(["mango","grapes"])

#remove function
list4.remove("banana")

#pop function
list4.pop()  #removes last element
list4.pop(1) #removes element at index 1
print(list4)


#del function
# del list4 
# print(list4)

#clear function
list5=[1,2,3,4,5]
list5.clear()
print(list5)

#while loop
list6=["a","b","c","d"]
i=0
while i<len(list6):
    print(list6[i])
    i+=1

#for loop
for item in list6:
    print(item)

fruits=["apple","banana","cherry"]
newlist=[x.upper() for x in fruits]
print(newlist)

newlist2=[x.capitalize() for x in fruits]
print(newlist2)

if("apple" in fruits):
    print("yes apple is present")

#sort function
fruits.sort()  #assending order
print(fruits)

fruits.sort(reverse=True) #descending order
print(fruits)

#reverse
list0=["Apple","cherry","banana"]
list0.reverse()
print(list0)

