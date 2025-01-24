
a = 2
b = 3
#arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  #remainder
print(a ** b)  #a ^b
#relational operators
#they give output either true or false
print(a == b)
print(a != b)
print(a <= b)
print(a < b)
print(a >= b)
print(a > b)
#assignment operator
num = 10
num = num + 5
print(num)
num += 5 #this is same as num = num + 5
print(num)
num -= 5
num *= 5
num /= 5
num **= 5 
print(num)
#logical operator
a = 50
b = 30
print(not False)
print(not (a > b))
val1 = True
val2 = False
print("and operator:", val1 and val2)
print("or operator:", val1 or val2)
print("or operator:", (a == b) or (a > b))

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