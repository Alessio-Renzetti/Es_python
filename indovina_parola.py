import random
'\u001b[32m'
'\u001b[33m'
'\u001b[31m'
def controllo(parola,parola1):
    str1=""
    for x in range(len(parola)):
        if parola[x]==parola1[x]:
            print("hai indovinato la lettera",parola[x],"ed è nella giusta posizione")
            str1+='\u001b[32m'+parola[x]
        elif (parola[x] in parola1)==True:
            print("hai trovato la lettera",parola_utente[x],"ma non è nella posizione corretta")
            str1+='\u001b[33m'+parola[x]
        else:
            print("la lettera",parola[x],"non è contenuta nella parola da indovinare")
            str1+='\u001b[31m'+parola[x]
    return str1+'\u001b[0m'
lista=["ansia", "balzo", "cielo", "dolce", "etere",
    "furia", "gusto", "husky", "igloo", "jeans",
    "karma", "lince", "miele", "notte", "odino",
    "piano", "quota", "renna", "scuro", "tetto",
    "umore", "verde", "water", "young",
    "zebra"]
parola_indovinare=lista[random.randint(0,25)]
parola_utente=""
parole_usate=""
for x in range(6):
    if x==0:
        parola_utente=str(input("Prova ad indovinare la parola da 5 lettere: "))
        if parola_utente==parola_indovinare:
            print("hai indovinato la parola in",x+1,"tentativi")
            break
        else:
            parole_usate=controllo(parola_utente,parola_indovinare)
    else:
        print(parole_usate)
        parola_utente=str(input("riprova ad indovinare la parola tenendo conto delle lettere sbagliate e quelle giuste "))
        if parola_utente==parola_indovinare:
            print("hai indovinato la parola in",x+1,"tentativi")
            break
        else:
            parole_usate=controllo(parola_utente,parola_indovinare)
