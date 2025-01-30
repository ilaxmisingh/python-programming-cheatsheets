str1 = 'lax'
str2 = 'mi'
final_str = str1 + str2
print(final_str)
print(len(str1))
# length also inculdes whitespces, signs etc in string lenght calculation
# indexing
str = 'laxmi singh'
ch = str[0]
print(ch)
# note that in indexing we can only access string , we cannot modify any string character
# slicing 
print(str[1:4]) # note that slicing include starting index and ending index as 1 and 4 respectively....now it will only include 1,2,3 position elements ...it will exclude 4th element.
print(str[0:len(str)]) # len(str) will give till last of the string
print(str[5:]) # this also means that we want to go till the last element 
#negative index
print(str[-4:-1])
