# if-elif-else
marks = int(input("Enter your marks:"))

if(marks >= 90):
    print("grade = 'A'")
elif(marks >= 80 and marks < 90):
    print("grade = 'B'")
elif(marks >= 70 and marks < 80):
    print("grade = 'C'")
else:
    print("grade = 'D'")
# odd or even
num = int(input("Enter your number:"))
if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")
# greatest of three numbers entered by the user 
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter third number:'))
if(num1> num2 and num1> num3):
    print("Num1 is largest")
elif(num2> num1 and num2> num3):
    print("Num2 is largest")
else:
    print("Num3 is largest")
#largest of four number
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter third number:'))
num4 = int(input('Enter fourth number:'))
if(num1> num2 and num1> num3 and num1 > num4):
    print("Num1 is largest")
elif(num2> num1 and num2> num3 and num2 > num4):
    print("Num2 is largest")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("Num3 is largest")
else:
    print("Num4 is the largest")
#write a program to check if the number is multiple of 7 or not
num = int(input("Enter your number:"))
if(num % 7 == 0):
    print("Multiple ")
else:
    print("not a multiple")