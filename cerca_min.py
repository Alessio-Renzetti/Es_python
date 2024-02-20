p=int(input("quante righe vuoi inserire all'interno della lista? "))
q=int(input("quante colonne vuoi inserire all'interno della lista? "))
min=2183274278942
lista = [[0 for _ in range(q)] for _ in range(p)]
pos_righe=0
pos_colonne=0
for i in range(p):
    for j in range (q):
        lista[i][j]=int(input("numero da inserire "))
for i in range(p):
    for j in range (q):
        if lista[i][j]<min:
            pos_righe=i
            pos_colonne=j
            min=lista[i][j]
print("il numero minore fra colonne è in posizione",pos_righe,pos_colonne)
print(lista)
min=2183274278942
for i in range(q):
    for j in range (p):
        if lista[j][i]<min:
            pos_righe=j
            pos_colonne=i
            min=lista[j][i]            
print("il numero minore fra righe è in posizione",pos_righe,pos_colonne)
print(lista)

