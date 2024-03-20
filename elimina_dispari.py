dizionario={
    "voti1": [5,8,7,6],
    "voti2": [3,8,10],
    "voti3": [7,7,7,10,7]
}

for i in dizionario:
    pos_remove=[]
    for y in range(len(dizionario[i])-1,-1,-1):
        if dizionario[i][y]%2==1:
            dizionario[i].remove(dizionario[i][y])
    

print(dizionario)