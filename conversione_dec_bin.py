result=""
def conversione(n):
    global result
    if n!=0:
        if n%2==0:
            result+="0"
            return conversione(n//2)
        else:
            result+="1"
            return conversione(n//2)
    return result
        
n=int(input("che numero vuoi convertire in binario? ")) 
app=conversione(n)   
n_binario=""
for x in range(len(app)-1,-1,-1):
    n_binario+=app[x]
print("il numero in binario è",n_binario)
