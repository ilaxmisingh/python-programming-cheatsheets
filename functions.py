#waf to print the length of a list
#(list is the parameter)

list1 = ["hii","my","hello"]
list2 = ["yes","no"]
def calc_len(list):
    print(len(list))
calc_len(list1)
calc_len(list2)

#wap to print the elements of a list in a single line.(list is the parameter)

list1 = ["hii","my","hello"]
list2 = ["yes","no"]
def print_list(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item, end = " ")
print_list(list1)
print_list(list2)

#waf to find the factorial of n
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
fact(5)

#waf to convert usd to inr

def conv(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR")

conv(1)
conv(2)    

