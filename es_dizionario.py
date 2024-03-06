dizionario={
    "uno":[1,2,3],
    "due":[4,5,76,54,789,32,334,665],
    "tre":[7,122,921],
    "quattro":[10,11,12,90,64,72],
    "cinque":[13,14,21],
    "sei":[16,17,18,45,73],
    "sette":[19,20,21,22]
}
chiave=""
minimo=10234453
lista=[]
for x in dizionario:
    if len(dizionario[x])<minimo:
        minimo=len(dizionario[x])
        chiave=x
for x in dizionario:
    if len(dizionario[x])==minimo:
        print(x)
        
