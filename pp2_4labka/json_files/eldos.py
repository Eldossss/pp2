import json  
with open ("example.json","r") as json_file:
    a  = json.load(json_file)
    
# print(a)
del a["3-rd type"]["Description"] #-> удалить элемент 

print(a)
