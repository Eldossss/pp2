#@PydevCodeAnalysisIgnore
#@PydevCodeAnalysisIgnore = True
#@PydevCodeBlock = False
import json 
with open("eldos.json", "r") as file:
    frota = file.read()
    reading = json.loads(frota)
    
tri = reading["imdata"] 
print("I N T E R F A C E__S T A T U S")
print("="*80)
print("DN", (" "*48), (" "*1), "Description", (" "*10), "Speed", (" "*3), ("MTU"))
print("-"*50,(" "*1),("-"*20),(" "*2),("-"*6),(" "*2),("-"*6))
for i in range(0,len(tri)):
    print(tri[i]["l1PhysIf"]["attributes"]["dn"],(" "*33), tri[i]["l1PhysIf"]["attributes"]["mtu"],(" "*4), tri[i]["l1PhysIf"]["attributes"]["speed"], end = "\n")
