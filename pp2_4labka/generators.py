
# 1
## # print(next(b))
    # print(next(b))
    # print(next(b))
    # print(next(b))
    # print(next(b))
    # print(next(b)) это пример как вводить элементы каждого генератора 
#  a  =  [i**2  for i in range (1,n+1)] - > it is a type of list with [] scope 
#  b = (i**2 for i in range (1,n+1)) -> it is a type of generator with() scope 
#  hint : Генератор только может делать только один обход 
# hint  : генератор состоит из итераторов в свою очередь итераторы работают по принципу next() 
#  hint : next() -  функция в свою очередь берет только 1 значение но у него есть особенность запоминкть следующий элемент 
# x = int(input("Enter the x: "))
# def genrators(x):
#     b =  (i**2 for i in range (1,x+1))
 # print(next(b))
#     for i in b :
#         print(i)
# genrators(x)

#2
# x = int(input("Enetr the x: "))
# def func(x):
#     b = (2*i for i in range(0,x))
#     for i in b:
#         print(i,end=",")
# func(x)

#3
# def divisible_by_3_and_4(n):
#     for num in range(n+1):
#         if num % 3 == 0 and num % 4 == 0:
#             yield num


# n = int(input())

# for number in divisible_by_3_and_4(n):
#     print(number)



#4


# def squares(x,y):
#     for number in range(x,y+1):
#         yield number**2

# x = int(input( "enter the x : "))
# y = int(input("enter the y :"))

# for square in squares(x,y):
#     print(square)



# import numpy as np
# x = int(input("Enter  x : "))
# def functator(x):
#     b  = (i for i in range(x,-1,-1))
#     print(b) #-> type = generator 
#     for i in b :
#         print(i)
# functator(x)



