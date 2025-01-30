#lists
marks = [96,45,78,34]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
student = ['name',90, 14,'london']
print(student)
#list slicing
print(marks[1:4])
print(marks[-3:-1])
#list methods 
list = [2,1,3]
print(list)
list.append(4) # adds an element at the end
print(list)
print(list.append(4)) # does not return any value
print(list)# therefore needs another print statement
list.sort() #sorts in ascending order
print(list)
list.sort(reverse = True) #sorts in descending order
print(list)
list.reverse() #reverses the string
print(list)
# note that sorting also applies on character and string
list.insert(1,8)#insert element at index
print(list)
list.remove(1)#remove first occurance of that number
print(list)
list.pop(4)# pop element of that index number
print(list)



#tuples
#tuples are immutable(unchangeable) and lists are mutuable(changeable)
tup = (2,1,3,2)
print(tup[0])
print(tup[1])
#tup[2] = 22 will give error because it i immutable
#for empty tuple
tup1 = ()
print(tup1)
print(type(tup1))
#for single tuple
tup2 = (1,) # if u remove comma then python will conside tup2 as integer not a tuple
print(tup2)
print(type(tup2))
#tuple slicing
print(tup[1:3])
#tuple methods

print(tup.index(2)) # returns the index of first occurance of the element
print(tup.count(2)) # returns count of the elemnt