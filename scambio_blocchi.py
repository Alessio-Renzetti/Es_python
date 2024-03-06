lista=[]
lista_scambiata=[[]]
respons=""
cond=""
cont=0
while cond!="si":
    n=int(input("quanti numeri vuoi inserire all'interno di questo blocco? "))
    for x in range(n):
        lista.append(int(input("che numero vuoi inserire all'interno della lista? ")))
    lista.append("#")
    cond=str(input("Hai finito di riempire la lista? Rispondi con: si/no "))
lista.pop()
for x in lista:
    if x == "#":
        # Appendi lista vuota e aggiorna contatore
        lista_scambiata.append([])
        cont += 1
    else:
        lista_scambiata[cont].append(x)

print(lista)
for i in range(1, len(lista_scambiata), 2):
    lista_scambiata[i-1], lista_scambiata[i] = lista_scambiata[i], lista_scambiata[i-1]
print(lista_scambiata)