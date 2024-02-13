def calcola_MCD(n1,n2):
    if n1==n2:
        return n1
    elif n1<n2:
        return calcola_MCD(n1,n2-n1)
    else:
        return calcola_MCD(n2,n1-n2)
n1=int(input("dimmi il primo numero "))
n2=int(input("dimmi il secondo numero "))
print(calcola_MCD(n1,n2))