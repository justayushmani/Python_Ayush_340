# creating a dictionary
d = {
    "name": "ram",
    "age": 20,
    "class": 5
}

print(d)
print(d["name"])
print(d["age"])
print(d["class"])

#getting keys
print(d.keys())

#getting values
print(d.values())

#searching element in dictionary
d.get("name")
d.get("age")
d.get("class")