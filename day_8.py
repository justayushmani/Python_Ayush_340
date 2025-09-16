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

