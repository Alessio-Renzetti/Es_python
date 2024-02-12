import random
giocatore=input("come ti chiami? ")
banchiere="Maurizio"
print("piacere sono",banchiere)
dado1=0
dado2=0
dado3=0
saldoB=20
saldoG=20
scommessa=[]
soldi=[]
casellescom=[]
caselle=[1,2,3,4,5,6]
turno=1
print("questo è il terreno di gioco")
print(caselle)
fine=False
while fine!=True:
    if saldoB==0:
        print("HAI VINTO $$$")
        fine=True
        break
    elif saldoG==0:
        print("HAI PERSO :(")
        fine=True
        break
    print("bene siamo nel turno",turno)
    s=int(input("su quante caselle vuoi scommettere "))
    if s>3 :
        print("hai superato il numero di caselle massime su cui scommettere")
        s=int(input("su quante caselle vuoi scommettere (max 3 caselle) "))
    for x in range(s):
        scommessa.insert(x,int(input("su quale casella vuoi scommetter? ")))
        print("i tuoi soldi attuali sono",saldoG)
        soldi.insert(x,int(input("quanti soldi vuoi scommettere? ")))
        saldoG=saldoG-soldi[x]
        if saldoG<=0:
            print("mi dispiace hai perso")
            fine=True
            break
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    dado3=random.randint(1,6)
    for x in range(len(scommessa)):
        if scommessa[x]==dado1 and scommessa[x]==dado2 and scommessa[x]==dado3:
            saldoG=saldoG+soldi[x]*3
            saldoB=saldoB-soldi[x]*2
            print("$ JACKPOT $")
            print("la",x+1,"scommessa è andata a segno il tuo saldo attuale è di",saldoG)
            print("il saldo del banchiere è invece di",saldoB)
            print(dado1)
            print(dado2)
            print(dado3)
        elif scommessa[x]==dado1 and scommessa[x]==dado2:
            saldoG=saldoG+soldi[x]*2
            saldoB=saldoB-soldi[x]*1
            print("la",x+1,"scommessa è andata a segno il tuo saldo attuale è di",saldoG)
            print("il saldo del banchiere è invece di",saldoB)
            print(dado1)
            print(dado2)
            print(dado3)
        elif scommessa[x]==dado2 and scommessa[x]==dado3:
            saldoG=saldoG+soldi[x]*2
            saldoB=saldoB-soldi[x]*1
            print("la",x+1,"scommessa è andata a segno il tuo saldo attuale è di",saldoG)
            print("il saldo del banchiere è invece di",saldoB)
            print(dado1)
            print(dado2)
            print(dado3)
        elif scommessa[x]==dado3 and scommessa[x]==dado1:
            saldoG=saldoG+soldi[x]*2
            saldoB=saldoB-soldi[x]*1
            print("la",x+1,"scommessa è andata a segno il tuo saldo attuale è di",saldoG)
            print("il saldo del banchiere è invece di",saldoB)
            print(dado1)
            print(dado2)
            print(dado3)
        elif scommessa[x]==dado3 or scommessa[x]==dado1 or scommessa[x]==dado2:
            saldoG=saldoG+soldi[x]
            print("la",x+1,"scommessa è andata a segno il tuo saldo attuale è di",saldoG)
            print("il saldo del banchiere è invece di",saldoB)
            print(dado1)
            print(dado2)
            print(dado3)
        else:
            saldoB=saldoB+soldi[x]
            print("la tua",x+1,"scommessa non è andata a segno il tuo saldo attuale è di",saldoG)
            print("il saldo del banchiere è invece di",saldoB)
            print(dado1)
            print(dado2)
            print(dado3)
    for x in range(len(scommessa)):
        scommessa.remove(scommessa[0])
        soldi.remove(soldi[0])
    turno+=1


