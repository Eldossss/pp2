
# 1

# x = int(input("Write the grams : "))
# def from_gram_to_ounces(x):
#     return x*28.3495231

# print(from_gram_to_ounces(x))



#2
# farangheit = float(input("Write farangheit temperature : "))

# def from_farengheit_to_celcius(farangheit):
#     return float(5/9)*(farangheit-32)


# print(from_farengheit_to_cencius(farangheit))


#3
# heads = int(input("Write a number of heads : "))
# legs = int(input("Write a number of legs : "))


# def solve(heads,legs):
#   for x in range(100):
#     if 2*x + 4*(heads-x) == legs:
#       petuhov = x
#       print("Number of petuhov :",petuhov)
#       break


#   for y in range(100):
#       if petuhov + y == heads:
#          krolikov = y
#          print("Number of krolikov : ",krolikov)
#          break
      
# solve(heads,legs)


4#


# x = int(input("Enter the size of the array  :"))
# array = list()
# prime_array = list()
# for i in range(0,x):
#     y = int(input())
#     array.append(y)
# cnt = 0 
# def functator(array,x,prime_array,cnt):
#     for i in range(0,x): 
#         for j in range(2,array[i]+1):
#             if array[i] % j == 0:
#                 cnt += 1
#         if cnt  == 1:
#             prime_array.append(array[i])
#         cnt = 0     
#     print(prime_array)
# functator(array,x,prime_array,cnt)    


#5


# string = str(input("Enter the string : "))
# def get_permutation(string,i = 0):
#     if i == len(string):
#         print("".join(string))
#     for j in range(i,len(string)):
#         words = [c for c in string]
#         words[i],words[j] = words[j],words[i]
#         get_permutation(words,i+1)
# get_permutation(string)


#6
# string  = str(input("Enter the string :  "))

# def future(string):
#     reversed_string  = ' '.join(string.split()[::-1])
#     print(reversed_string)
# future(string)    


#7
# def func1(x,array):
#     for i in range(0,x):
#         y = int(input())
#         array.append(y)     

# def func2(x,array,cnt):
#     for i in range(0,x):
#         if array[i]== 3 and array[i+1] == 3:
#             cnt += 1
#     if cnt > 0:
#         return True
#     else :
#         return False

# x = int(input("Enter the size of the  array : "))
# array = list()
# cnt = 0
# func1(x,array)
# if func2(x,array,cnt):
#     print("True")
# else :
#     print("False")    


8#
# x = int(input("Enter the size of the array : "))
# array = list() 
# for i in range(0,x):
#     y = int(input())
#     array.append(y)
# unique_array =  list()    
# for i in range(0,x):
#     if array[i] == 0 or array[i] == 7:
#         unique_array.append(array[i])

# def functator(unique_array):
#     stringa = ' '.join(map(str,unique_array))
#     if "0 0 7" in stringa:
#         return True
#     else :
#         return False
# print(functator(unique_array))


9#
# x = float(input("Enter the radius of a sphere : "))

# def volume(x):
#       return 4/3 * 3.14*x**3

# print(volume(x))


#10
# x = int(input("Emter the size of the array : "))
# array = list()
# for i in range(0,x):
#     y = int(input())
#     array.append(y)
# unique_array = list()

# def func(array,x,unique_array):
#     for i in range(0,x):
#         for j in range(i+1,x):
#             if array[i] == array[j]:
#                 array[j] = -1
#     for i in range(0,x):
#         if array[i] != -1:
#             unique_array.append(array[i]) 
#     print(unique_array)
# func(array,x,unique_array) 


#11

# def is_palindrome(string):
#     reversed_string = string[::-1]
#     return string == reversed_string  # boolean  value #


# word  = str(input("Enter the string : "))
# if  is_palindrome(word):
#     print(f"{word}  is a palindrome .")

# else :
#     print(f"{word} is not a palindrome . ")  

# 12#

# def frucin0(x, y, z):
#     for i in range(0, x):
#         print("*", end="")
#     print()  #

#     for j in range(0, y):
#         print("*", end="")
#     print()  

#     for k in range(0, z):
#         print("*", end="")
#     print() 

# x = int(input("Enter the x: "))
# y = int(input("Enter the y: "))
# z = int(input("Enter the z: "))
# frucin0(x, y, z)


13#

# import random
# def guess_number():
#     print("Hello lets play randomizer play : ")
#     print("Whtas your name ? ")
#     x = str(input())
#     print(f"Well {x} im thinking of a number between 1 - 20")
#     number =  random.randint(1,20)
#     guess = 0 
#     counter  = 0 

#     while guess != number :
#         guess = int(input("Take a  guess : "))
#         counter =  counter  + 1 


#         if guess < number :
#             print("Your number is to low . ")

#         elif guess > number :
#             print("Your number is to high . ")

#         else :
#             print (f"Good  job {x} , you guessed my number in {counter}, guesses!")   
# guess_number()    





