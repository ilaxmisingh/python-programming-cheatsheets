#ask the user to enter names of their three fav movies and store them in a list
# mov1 = input("Enter ur first fav:")
# mov2 = input("Enter ur second fav:")
# mov3 = input("Enter ur third fav:")
# list = [mov1,mov2,mov3]
# print(list)
movies = []
mov1 = input("Enter ur first fav:")
mov2 = input("Enter ur second fav:")
mov3 = input("Enter ur third fav:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#check if a list contains palindrome or not

list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("It is a palindrome")
else:
    print("It is not palindrome")

#count the number of students with "a " grade in the following tuple =(c,d,a,a,b,b,a)
tup = ('c','d','a','a','b','b','a')
print(tup.count('a'))
list = ['c','d','a','a','b','b','a']
list.sort()
print(list)