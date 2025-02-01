info = {
    "key" : "value",
    "name" : "laxmi",
    "learning" : "coding"
}
print(info)
print(info["name"])

#changing value
info["name"] = "singh" #overwrite ,it overwrites the values in original dictionary

print(info["name"])
null = {}
print(null)
null["name"] = "xyz"
print(null)

#nested dictionary
student = {
    "name" : "laxmi",
    "subjects" : {
        "phy" : 45,
        "chem" : 67,
        "math" : 100
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

#dictonary methods

print(student.keys())
print(len(list(student.keys())))

print(student.values())
#print(student["name2"]) throws an error
print(student.get("name2"))
student.update({"city" : "delhi"})
print(student)