#type conversion
# here the python interpreter has automatically converted a (int) into float 
a = 2 
b = 3.14
sum = a + b
print(sum)
print(type(sum))
print(type(a))
#type casting
# here we need to convert manually
'''
a = "2" # string
b = 3.14
sum = a + b
print(sum)
print(type(sum))
print(type(a))
 #this prints an error because string cannot be added to float automatically
 '''

b = 3.14
a = float('2')
sum = a + b
print(sum)
print(type(sum))
print(type(a))