lista=[[1,"Pippo",7],[2,"Carlo",14],[3,"Gianluca",3],[4,"Pollo",3]]
dizionario={}
for x in range(len(lista)):
    for y in range(len(lista[x])):
        dizionario[lista[x][0]]=lista[x][1 :]
print(dizionario)