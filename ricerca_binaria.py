import random
def media(n1,n2):
    med=int(0)
    med=n1+n2
    return int(med/2)
def ordina_lista(lista):
    n=len(lista)
    app=0
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                app=lista[j]
                lista[j]= lista[j+1]
                lista[j+1] = app
lista=[]
numero=0
flag=False
flag1=False
pos=0
n=int(input("quanti numeri vuoi inserire all'interno della lista? "))
for x in range(n):
    lista.insert(x,int(input("inserisci un numero ")))
ordina_lista(lista)
numero=int(input("che numero cerchi? "))
indiceMax=len(lista)
indiceMin=0
while flag1!=True:
    if numero==lista[0] :
        pos=0
        flag=True
        break
    elif numero==lista[n-1]:
        pos=n-1
        flag=True
        break
    else:
        if numero==lista[media(indiceMin,indiceMax)]:
            flag=True
            break
        elif numero>lista[0] and numero<=lista[media(indiceMin,indiceMax)]:
            indiceMax=media(indiceMin,indiceMax)
            if numero==lista[media(indiceMin,indiceMax)]:
                pos=media(indiceMin,indiceMax)
                flag=True
                break
            elif numero>lista[0] and numero<lista[media(indiceMin,indiceMax)]:
                indiceMax=media(indiceMin,indiceMax)
                if numero==lista[media(indiceMin,indiceMax)]:
                    pos=media(indiceMin,indiceMax)
                    flag=True
                    break
            elif numero>lista[media(indiceMin,indiceMax)/2] and numero<=lista[media(indiceMin,indiceMax)]:
                indiceMin=media(indiceMin,indiceMax)/2
                indiceMax=media(indiceMin,indiceMax)
                if numero==lista[media(indiceMin,indiceMax)]:
                    pos=media(indiceMin,indiceMax)
                    flag=True
                    break
        elif numero>lista[media(indiceMin,indiceMax)]  and numero<lista[n-1]:
            indiceMin=media(indiceMin,indiceMax)
            if numero==lista[media(indiceMin,indiceMax)]:
                pos=media(indiceMin,indiceMax)
                flag=True
                break
            elif numero>lista[indiceMin] and numero<lista[media(indiceMin,indiceMax)]:
                indiceMax=media(indiceMin,indiceMax)
                if numero==lista[media(indiceMin,indiceMax)]:
                    pos=media(indiceMin,indiceMax)
                    flag=True
                    break
            elif numero>lista[media(indiceMin,indiceMax)] and numero<lista[n-1]:
                indiceMin=media(indiceMin,indiceMax)
                if numero==lista[media(indiceMin,indiceMax)]:
                    pos=media(indiceMin,indiceMax)
                    flag=True
                    break
    flag1=True
if flag==True:
    print("il numero che cerchi è presente nella lista in posizione",pos)
    print(lista)
else :
    print("il numero che cerchi non è presente nella lista ")
    print(lista)
    


                

    
       

    

