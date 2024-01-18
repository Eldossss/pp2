#1

class Fortrane:
   
    def get_String(self):
        self.stringachok = input()

    def print_String(self):
        print(self.stringachok.upper())

stringachok = Fortrane()
stringachok.get_String()
stringachok.print_String()



#2,3 problem in one case subclass Rectangle and subclass Square

class Shape:
   PI = 3.14
   def area(self, Area):
      self.Area = Area
      print(f"Area of a shape  :  {self.Area}")


class Square(Shape):
   def __init__(self, length, side):
      self.length = length
      self.side = side

   def area1(self):
       return self.side**2

class Rectangle(Shape):
   def __init__(self,length1,width1):
      self.length1 = length1
      self.width1 = width1

   def area2(self):
     return self.length1*self.width1
     
 
area_of_a_shape = Shape()
Area = 0
area_of_a_shape.area(Area)

length = int(input("Enter the value of length: "))
side = length / 4
square1 = Square(length,side)
print("The are of the square  = ", square1.area1())

length1 = int(input("Enter the length of a rectangle : "))
width1 = int(input("Enter the width of a rectangle : "))
rectangle1 = Rectangle(length1,width1)
print("The are of a rectangle = ", rectangle1.area2())



#4
import math

class Point:
   def __init__(self, x, y, x1, y1):
      self.x = x
      self.x1 = x1
      self.y = y
      self.y1 = y1

   def show(self):
      print(f"X is equal to: {self.x}")
      print(f"Y is equal to: {self.y}")

   def move(self):
      print(f"After moving X1 is equal to: {self.x1}")
      print(f"After moving Y1 is equal to: {self.y1}")

   def dist(self):
      return math.sqrt((self.x - self.x1) ** 2 + (self.y - self.y1) ** 2)

x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
x1 = int(input("Enter the value of X1: "))
y1 = int(input("Enter the value of Y1: "))

coordinates = Point(x, y, x1, y1)
coordinates.show()
coordinates.move()
print(coordinates.dist())

#5
class Bank_Account:
   def __init__(self,owner,balance):
      (self.owner)  = owner
      self.balance = balance

   def deposit(self,amount):
      if amount > 0:
         self.balance += amount
         print(f"Mister {self.owner} the operation was successful . Your current balanca : {self.balance}")
      else :
         print(f"Mister {self.owner} you cannot send negative deposit!!!")
   def withdraw(self,amount):
      if  amount > 0:
         if amount < self.balance:
            self.balance -= int(amount)
            print(f"Mister {self.owner} the operation was successful . Your current balance : {self.balance}") 
         else :
            print(f"Mister {self.owner} your current balance is : {self.balance} and you cannot take {amount} money!!! ")
      else :
         print(f"Mister {self.owner} you cannot get negative withdraw!!!")

name = str(input("Your name please : "))
balance = int(input("Your balance please : "))
deposit1 = int(input(f"Mister {name} enter your deposit please : "))
withdraw1 = int(input(f"Mister {name} enter your withdraw please : "))
Account = Bank_Account(name,balance)
Account.deposit(deposit1)
Account.withdraw(withdraw1)


#6

x = int(input("Enter the size of the array: "))
array = []
for i in range(x):
    y = int(input())
    array.append(y)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_array = list(filter(lambda num: is_prime(num), array))

print("Prime numbers:", prime_array)

