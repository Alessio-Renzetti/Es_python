def copia_dizionario(dizionario):
    D={}
    for x in dizionario:
        if dizionario[x] in D:
            D[dizionario[x]]+=1
        else:
            D[dizionario[x]]=1
    return D    
dizionario={
    "chiave1":10,
    "chiave2":20,
    "chiave3":10,
    "chiave4":15,
    "chiave5":15,
    "chiave6":10
}
diz=copia_dizionario(dizionario)
print(diz)