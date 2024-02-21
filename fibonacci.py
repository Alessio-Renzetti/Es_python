def sez_aurea(n,app):
    if n>1:
        return sez_aurea(n-1,app)+sez_aurea(n-2,app)
    elif n==0:
        return 0
    else:
        return 1/seq_fibonacci(app)



def seq_fibonacci(n):
    if n>1:
        return seq_fibonacci(n-1)+seq_fibonacci(n-2)
    elif n==0:
        return 0
    else:
        return 1

n=int(input("in che posizione vuoi cercare il numero? "))
print("il numero che cercavi è",seq_fibonacci(n))
print("la sezione aurea è",sez_aurea(n,n-1))
    