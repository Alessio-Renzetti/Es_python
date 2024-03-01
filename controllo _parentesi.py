def espressione_parentesi(espressione,i):
    if espressione[i]=='(':
        return espressione_parentesi(espressione[i+1 :],i)
    elif espressione[i]==')':
        return calcolo(espressione[: i])
    else:
        return espressione_parentesi(espressione,i+1)


def calcolo(espressione):
    lista=[]
    app=""
    poSim=[]
    tot=0   
    for x in range(len(espressione)):
        if espressione[x]=='0' or espressione[x]=='1' or espressione[x]=='2' or espressione[x]=='3' or espressione[x]=='4' or espressione[x]=='5' or espressione[x]=='6' or espressione[x]=='7' or espressione[x]=='8' or espressione[x]=='9':
            app=app+espressione[x]
        else :
            lista.insert(len(lista),app)
            poSim.insert(len(poSim),int(x))
            app=""
        if x==len(espressione)-1:
            lista.insert(len(lista),app)
    for i in range(len(lista)-1):

        if espressione[poSim[i]]=='+':
            tot=somma(lista[0],lista[1])
            lista.remove(lista[0])
            lista.remove(lista[0])
            lista.insert(0,tot)
        if espressione[poSim[i]]=='-':
            tot=sott(lista[0],lista[1])
            lista.remove(lista[0])
            lista.remove(lista[0])
            lista.insert(0,tot)
        if espressione[poSim[i]]=='*':
            tot=prod(lista[0],lista[1])
            lista.remove(lista[0])
            lista.remove(lista[0])
            lista.insert(0,tot)
        if espressione[poSim[i]]=='/':
            tot=div(lista[0],lista[1])
            lista.remove(lista[0])
            lista.remove(lista[0])
            lista.insert(0,tot)
    return tot 
def somma(a,b):
    tot=int(a)+int(b)
    return tot
def sott(a,b):
    tot=int(a)-int(b)
    return tot
def prod(a,b):
    tot=int(a)*int(b)
    return tot
def div(a,b):
    tot=int(a)/int(b)
    return tot
espressione=str(input("inserisci un espressione complessa "))
contP=0
flag=True
i=0
pos=0
while flag!=False:
    if i<len(espressione) and contP>=0:
        if espressione[i]=='(':
            contP+=1
            pos=i
            
        if espressione[i]==')':
            contP-=1
        i+=1
    else:
        if contP==0:
            
            break
        else:
            
            break
# for x in range(len(espressione)):
#     if espressione[x]=='*':
#         app="("+espressione[x-1]+espressione[x+1]+")"

print(calcolo(espressione[: pos]),espressione_parentesi(espressione,pos))
