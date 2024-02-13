def calcola_MCD(n1,n2):
    if n1==n2:
        return n1
    elif n1<n2:
        return calcola_MCD(n1,n2-n1)
    else:
        return calcola_MCD(n2,n1-n2)
n1=27
n2=45
print(calcola_MCD(n1,n2))