def merge(lista):
    if len(lista)<=1:
        return lista
    lista_1=lista[0:len(lista)//2]
    lista_2=lista[len(lista)//2:]

    app1=merge(lista_1)
    app2=merge(lista_2)

    lista_ord=ordinamento(app1,app2)
    return lista_ord

def ordinamento(lista_1, lista_2):
    lista_finale = []
    i = 0
    j = 0
    while i < len(lista_1) and j < len(lista_2):
        if lista_1[i] <= lista_2[j]:
            lista_finale.append(lista_1[i])
            i += 1
            continue
        lista_finale.append(lista_2[j])
        j += 1

    while i < len(lista_1):
        lista_finale.append(lista_1[i])
        i = i + 1
        
    while j < len(lista_2):
        lista_finale.append(lista_2[j])
        j = j + 1
        
    return lista_finale
lista=[2,5,1,7,4,8,12,6]
lista_ordinata=merge(lista)
print(lista_ordinata)