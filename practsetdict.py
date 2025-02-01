#store the following word meanings in a python dictionary
dict = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}
print(dict)

set = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(set))
 #wap to enter marks of 3 subjects from the user and store them in a dictionary.
marks = {}
x = int(input("enter phy:"))
marks.update({"phy" : x})
x = int(input("enter math:"))
marks.update({"math" : x})
x = int(input("enter chem:"))
marks.update({"chem" : x})
print(marks)