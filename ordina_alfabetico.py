def ordine_alfabetico(parola1,parola2):
    if len(parola1)!=0 and len(parola2)!=0: 
        if parola1[0]>parola2[0]:
            return parola2[0]+ordine_alfabetico(parola1.replace(parola1[0],""),parola2.replace(parola2[0],""))
        elif parola1[0]<parola2[0]:
            return parola1[0]+ordine_alfabetico(parola1.replace(parola1[0],""),parola2.replace(parola2[0],""))
        else:
            return parola1[0]+ordine_alfabetico(parola1.replace(parola1[0],""),parola2.replace(parola2[0],""))
    else:
        return ""
parola1=str(input("digita una parola "))
parola2=str(input("digita una parola "))
print(ordine_alfabetico(parola1,parola2))