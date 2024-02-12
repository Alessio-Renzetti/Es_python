import random
#primo lancio 7==win 2or12==lose se fai un altro numero diventa la condizione di vittoria e con il 7 perdi
ris=[]
flag=False
flag1=False
while flag!=True:
    
    if flag1==False:
        x=0
        flag1=True
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        ris.insert(x,dado1+dado2)
        if ris[x]==7:
            flag=True
            print("hai vinto perchè è uscito",ris[x])
            print("i tuoi lanci sono stati",ris)
            break
        elif ris[x]==12 or ris[x]==2:
            flag=True
            print("hai perso perchè è uscito",ris[x])
            print("i tuoi lanci sono stati",ris)
            break
    else:
        x+=1
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        ris.append(dado1+dado2)
        if ris[0]==ris[x]:
            flag=True
            print("hai vinto perchè è uscito",ris[x])
            print("i tuoi lanci sono stati",ris)
            break
        elif ris[x]==7:
            flag=True
            print("hai perso perchè è uscito",ris[x])
            print("i tuoi lanci sono stati",ris)
            break

        