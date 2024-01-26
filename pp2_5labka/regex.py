1#
# import re
# txt = input("ENter the string : ")
# match =  re.findall(r"a+b*",txt)
# print(match)


2#
# import re
# txt  = str(input("ENter the sting : "))
# match =  re.findall(r"a+b{2,3}",txt)
# print(match)


3#
# import re

# txt = input("Enter the string: ")
# match = re.findall(r"([a-z]+(?:_[a-z]+)*)", txt)
# print(match)


#4

# import re
# txt = str(input('Enter the string  : '))
# match  = re.findall(f"[A-Z][a-z]+",txt)
# print(match)


#5

# import re
# txt =  str(input("Enter the string :  "))
# match = re.findall(r"^[a]+[a-zA-Z]*[b]+$",txt)
# print(match)


#6
# import re

# txt = str(input("Enter the string : "))

# match = re.sub(r'[ ,.]', ':', txt)

# print(match)


#7
#SNAKE CASE STRING :  ОЛ : hello_eldos
#CAMEL CASE STRING  : ОЛ : helloEleke бириниши создын биринши арып всегда кишкентай болады 
# def sake_to_cameke(sake):
#     words = sake.split('_')
#     cameke = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
#     return cameke

# sake = str(input('Enter the string : '))
# cameke = sake_to_cameke(sake)
# print(cameke)


#8
# import re

# txt = str(input('enter the string : ))   
# txt1 = re.findall('[A-Z][^A-Z]*', string)
# print(split_words)


#9
# import re

# txt = str(input("ENter the string : "))
# txt1 = ' '.join(re.findall(r'[A-Z][a-z]*', txt))
# print(txt1)


#10
# cameke = str(input('enter te camel string  : '))
# cameke  = cameke[0].lower() + cameke[1:]

# for i in cameke:
#     if i.isupper():
#         cameke = cameke.replace(i,f"_{i.lower()}")

# sake = cameke
# print(sake)