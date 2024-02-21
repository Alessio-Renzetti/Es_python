def seq_fibonacci(n):
    if n>1:
        return seq_fibonacci(n-1)+seq_fibonacci(n-2)
    elif n==0:
        return 0
    else:
        return 1

n=int(input("in che posizione vuoi cercare il numero? "))
print(seq_fibonacci(n))    