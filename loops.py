
#loops are used to repeat instructions
#while loop and for loop are there in python
count = 1 #count is an iterator
while count <= 5:
    print('Hello')
    count += 1
i = 5
while i >= 1:
    print(i)
    i -= 1
 # print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
#print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
#print the multiplication table of a number
i = 1
mul = 1
n = int(input("Enter n:\n"))
while i <= 10:
    mul = n * i
    print(mul)
    i += 1
#print the elements of the following list using loop : [1,4,9,16,25,36,49,64,81,100]
list = []
n = 1
while n <= 10:
    sqr = n * n
    print(sqr)
    n += 1
    list.append(sqr)
print(list)
#this is not the ideal way
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx <= len(idx):
    print(nums[idx])
    idx += 1
# another method
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
#search for a number x in this tuple using loop:[1,4,9,16,25,36,49,64,81,100]
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found aat idx",i)
    else:
      print("finding") 
    i += 1
#break and continue
i = 0
while i <= 5:
    if(i==3):
        i += 1
        continue
    print(i)
    i += 1
i = 0
while i <= 5:
    if(i == 3):
        break
    print(i)
    i += 1
#for loop
veggies = ["potato","tomato","carrot"]
for val in veggies:
    print(val)

#print the list
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in list:
    print(i)

#search for the given number in list
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
for el in nums:
    if (el == x):
        print("found", idx)
    idx += 1
    
#range () functions
for i in range(10):
 print(i)
#this range indicates stop 

for i in range(2,10):
    print(i)
#range(start and stop )

#start is included and stop is not included

for i in range(2,10,2):
    print(i)
here it is start,stop and step where step is the number with which it increases

#print odd numbers from 1 to 10

for i in range(1,10,2):
    print(i)
    
#print even numbers

for i in range(2,10,2):
    print(i)

#pass statement

for i in range(5):
    pass
print("some useful work")

#wap to find the sum of first n numbers(using while)

 n = 5
 sum = 0
 for i in range(1,n+1):
     sum += i
 print(sum)
#using while loop

 n = 7
 sum = 0
 i = 1
 while i <= n:
     sum += i
     i += 1
 print("total sum =", sum)
#wap to find the factorial of first n numbers(using for)
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    i += 1
print(fact)

