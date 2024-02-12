lista_num=input("inserisci un numero in binario ")
num_dec=0
pos=0
for x in range(len(lista_num)-1,-1,-1):
    print(lista_num[pos], x)
    app=int(lista_num[pos])*(2**x)
    num_dec=num_dec+app
    app=0
    pos+=1
print("il numero in base 10 è",num_dec)
