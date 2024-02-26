1
import re
txt = input("ENter the string : ")
match =  re.findall(r"a+b*",txt)
print(match)


2#
import re
txt  = str(input("ENter the sting : "))
match =  re.findall(r"a+b{2,3}",txt)
print(match)


3#
# import re

txt = input("Enter the string: ")
match = re.findall(r"([a-z]+(?:_[a-z]+)*)", txt)
print(match)


#4

# 
import re 
import sys 
import  os 
x = str(input())
txt = re.findall(r"^[A-Z]+[a-z]*",x)
print(txt)



#5


import re 
x = "ab" 
txt  = re.match(r"^a+\w?b+$",x)
print(txt.group())



#6


import re 
x = str(input())
txt = re.sub('[ .,]+', ':', x)
print(txt)


#7

import re 
import sys 
import os  
txt = str(input())
count = 0 
for i in range(0,len(txt)):
    if txt[i] == "_":
        count = i

modified =txt[0].lower() + txt[1:count+1] + txt[count+1:count+2].upper() + txt[count+2:]
pro_modified = modified.replace("_","")
print(pro_modified)
print(modified_txt)

#8

import re
import os 
import sys 
x = str(input())
txt  = ' '.join(re.findall(r"[A-Z]+[a-z]*",x))
txt = txt.split(" ")
print(txt)

#9
import re 
import sys 
import math 
x = str(input())
txt =  ' '.join(re.findall(r"[A-Z]+[a-z]*",x))
print(txt)



#10
import sys 
import math 
import re 
import os 
x = str(input())
xy = x[0].upper() + x[1:]
txt = ' '.join(re.findall(r"[A-Z][a-z]*",xy))
txt = txt[0].lower()  + txt[1:]
for i in range(0,len(txt)):
    if txt[i] == " ":
        count = i
txt = txt[0:count] + "_" + txt[count+1:count+2].lower()  + txt[count+2:]
print(txt)  