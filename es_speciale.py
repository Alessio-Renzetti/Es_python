lista=[
    ["titolo","autore","prezzo","copie_possedute"],
    ["1984","George Orwell","11",3],
    ["La chiamata dei tre","Stephen King","13",1],
    ["Il nome della Rosa","Umberto-erto-erto","15",0]
]
lista_di_libri=[]
for x in range(1,len(lista)):
    lista_di_libri.append({})
for j in range(len(lista_di_libri)):
    for i in range(len(lista)):
        lista_di_libri[j][lista[0][i]]=lista[j+1][i]
print(lista_di_libri)