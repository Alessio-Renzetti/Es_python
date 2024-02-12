cont=0
def risolvi (n,A,B,C):
    global cont
    cont+=1
    print(cont)
    if n==1:
        print("muovo il disco 1 da",A,"a",B)
        return
    risolvi(n-1,A,C,B)
    print("muovo il disco",n,"da",A,"a",B)
    

n=int(input("quanti dischi vuoi inserire? "))
risolvi(n,"A","C","B")
