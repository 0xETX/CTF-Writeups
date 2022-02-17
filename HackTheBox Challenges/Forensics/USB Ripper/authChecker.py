import json

file = open("syslog", "r")
text = file.read()

jsonfile=open("auth.json", "r")
jsonfileContents = jsonfile.read()
jsonProd = json.loads(jsonfileContents)['prod']
jsonManu = json.loads(jsonfileContents)['manufact']
jsonSerial = json.loads(jsonfileContents)['serial']

serialNum = []
manufac = []
product = []

for x in text.splitlines():
    if "SerialNumber: " in x:
        serialNum.append(x.split("SerialNumber: ")[1].strip())
    elif "Manufacturer: " in x:
        manufac.append(x.split("Manufacturer: ")[1].strip())
    elif "Product: " in x:
        product.append(x.split("Product: ")[1].strip())

for x in range(len(serialNum)):
    if serialNum[x] not in jsonSerial:
        print("Serial: "+serialNum[x])

for x in range(len(manufac)):
    if manufac[x] not in jsonManu:
        print("Manufac: "+manufac[x])
        
for x in range(len(product)):
    if product[x] not in jsonProd:
        print("Product: "+product[x])