
def conversione(n):
    if n!=0:
       return str(conversione(n//2))+str(n%2)
    else:
        return ""
n=int(input("che numero vuoi convertire in binario? ")) 
app=conversione(n)   
n_binario=""
print("il numero in binario è",app)