

# 1#
# array = list()
# x = int(input('Enter the size of the array : '))
# def functator(array,x):
#     for i in range(0,x):
#         y = int(input())
#         array.append(y)
#     print(sum(array))
# functator(array,x)



2#
# txt = str(input("Enter the string : "))
# cnt = 0 
# cnt1 = 0 
# def functator(txt,cnt,cnt1):
#     for chr in txt:
#         if chr.islower():
#             cnt +=1
#         elif chr.isupper():
#             cnt1 += 1
#     print(f"Number if lowercase letters : {cnt}")
#     print(f"Number of uppercase letters : {cnt1}")
# functator(txt,cnt,cnt1)


#3

# txt =  str(input("Enter the string : "))
# def isPalindrome(txt):
#     reversed_string = txt[::-1]
#     return reversed_string == txt

# if isPalindrome(txt):
#     print("Palindrome")
# else:
#     print("Not palindrome")




4
# import numpy as np
# import time 
# x = int(input("Enter the number  ; "))
# y = int(input("Enter the milliseconds ; "))
# time.sleep(y/1000)
# def func(x,y):
#   print(f"Square root of {x} after {y} miliseconds is:", np.sqrt(x))

# func(x,y)



#5
# x = (True,False,True,False,True,False,False,True,False,True,False,True,False)
# result = all(x)
# print(result)