# string functions
# 1.endswith
str = "laxmi singh"
print(str.endswith("er")) # false
print(str.endswith("ingh")) # true
# 2. capitalize - it capitalizes first character.
print(str.capitalize()) # in order to make first character capital python will create a new string and then make its first letter csptital
# if we want to make changes in original str , then 
str = str.capitalize()
print(str)
# replace function - replace string  with new value
print(str.replace('a', 'c'))
print(str.replace('singh', '.')) # it can also replace substrings
#find - returns 1st index of 1st occurence
print(str.find('a'))
print(str.find('c'))
print(str.find('Laxmi'))
#count
print(str.count('L'))





