#lists and dictionary cannot be stored in sets because they are mutable
#set are mutable but set's elements are immutable and unordered ...no duplicate values are there ..so it ignores duplicate values

collection = {1,2,3,4}
print(collection)
print(len(collection))
print(type(collection))
'''
collections = set() #emptyset
collections.add(1)
collections.add(4)
collections.remove(4)
collections.clear()#clears all the values
collections.pop() #generates random value from set
print((collections))


'''
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
