def controllo(lista,lista2,pos,pos2):
    if pos2==0:
        print("la seconda lista è contenuta nella prima al contrario")
        return True
        
    elif pos==len(lista)-1:
        print("la seconda lista non è contenuta nella prima al contrario")
        return False
        
    if lista[pos]==lista2[pos2]:
        return controllo(lista,lista2,pos+1,pos2-1)
    else:
        return controllo(lista,lista2,pos+1,pos2)
    

        



lista=[1,18,3,4,3,4,0]
lista2=[4,3,18]
controllo(lista,lista2,0,len(lista2)-1)