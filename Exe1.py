data = open("data.csv").read().rstrip()
lines = data.split("\n")
for l in lines:
    temp = l.split(",")
    if temp[0] == "Drosophila melanogaster" or temp[0] == "Drosophila simulans":
        print('The species'+temp[0]+'have gene'+temp[2])

for l in lines:
    temp = l.split(",")
    if len(temp[1]) >= 90 and len(temp[1]) <= 110:
        print("The lenth of "+temp[0]+"Gene "+temp[2]+" is between 90-110")


for l in lines:
    temp = l.split(",")
    if temp[1].upper().count("A")+temp[1].upper().count("T") < len(temp[1])/2:
        print(f'{temp[0]} AT content is less than 0.5')
    if int(temp[3]) > 200:
        print(f'{temp[0]} gene {temp[3]} expression level is greater than 200')

for l in lines:
    temp = l.split(",")
    if temp[1].upper().count("A")+temp[1].upper().count("T") < len(temp[1])/2:
        print(f'{temp[0]} AT content is less than 0.5')
    if int(temp[3]) > 200:
        print(f'{temp[0]} gene {temp[3]} expression level is greater than 200')


for l in lines:
    temp = l.split(",")
    if temp[1].upper().count("A")+temp[1].upper().count("T") < len(temp[1])*0.45:
        print(f'{temp[0]} AT content is low')
    elif temp[1].upper().count("A")+temp[1].upper().count("T") > len(temp[1])*0.65:
        print(f'{temp[0]} AT content is high')
    else:
        print(f'{temp[0]} AT content is mediunm')


