def trova_num(n,k):
    if k==0 or k==n:
        return 1 
    # elif k==1:
    #     return n
    # elif k==n-1:
    #     return n
    else:
        return trova_num(n-1,k-1)+trova_num(n-1,k)
n=int(input("In che riga vuoi cercare il numero "))
k=int(input("In che colonna vuoi cercare il numero "))
if k>n:
    k=int(input("hai inserito un numero di colonne errato inseriscine uno corretto "))
    print("Il numero che cerchi è",trova_num(n,k))
else:
    print("Il numero che cerchi è",trova_num(n,k))
#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1
#1 5 10 10 5 1
#1 6 15 20 15 6 1