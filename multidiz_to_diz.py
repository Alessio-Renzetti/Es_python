dizionario={
    "Riccardo":15,
    "Coso":20,
    "Ciccio":25
}
dizionario2={
    "Coso":22,
    "Ciccio":10
}
diz={}
for x in dizionario2:
    for y in dizionario:
        if x==y:
            diz[x]=[dizionario[y],dizionario2[x]]
        else:
            diz[y]=[dizionario[y]]
print(diz)