def criptare(frase,chiave,chiave2,cont):
    if len(frase)!=0:
        if cont%2==0:
            return chr(ord(frase[0])+chiave)+criptare(frase[+1 :],chiave,chiave2,cont+1)
        else:
            return chr(ord(frase[0])+chiave2)+criptare(frase[+1 :],chiave,chiave2,cont+1)
    else:
        return ""
def decriptare(frase,chiave,chiave2,cont):
    if len(frase)!=0:
        if cont%2==0:
            return chr(ord(frase[0])-chiave)+decriptare(frase[+1 :],chiave,chiave2,cont+1)
        else:
            return chr(ord(frase[0])-chiave2)+decriptare(frase[+1 :],chiave,chiave2,cont+1)
    else:
        return ""
frase=str(input("che frase vuoi criptare o decriptare "))
chiave=int(input("dammi la chiave di criptazione o decriptazione "))
chiave2=int(input("dammi la seconda chiave di criptazione o decriptazione "))
print(criptare(frase,chiave,chiave2,0))
print(decriptare(criptare(frase,chiave,chiave2,0),chiave,chiave2,0))