import random

parzyste=0
nieparzyste=0
zera=0
licznik=0

while True:
    liczba=random.randint(0,100)
    licznik+=1
    
    if liczba==0:
        zera+=1
    elif liczba%2==0 and liczba!=0:
        parzyste+=1
        if parzyste==20 and nieparzyste<20: ### drugi człon nie jest w rzeczywistości potrzebny
            print("Parzyste pierwsze!")
            break

    else:
        nieparzyste+=1
        if nieparzyste==20 and parzyste<20:  ### drugi człon nie jest w rzeczywistości potrzebny
            print("Nieparzyste pierwsze!")
            break

        
print("Wylosowanych zer:", zera, ". Wylosowanych liczb parzystych:", \
      parzyste,". Wylosowanych liczb nieparzystych:", nieparzyste, \
##      ". Łącznie było trzeba tylu losowań:", licznik)

while (nieparzyste!=20 and parzyste<20) or (parzyste!=20 and nieparzyste<20):  
    liczba=random.randint(0,100)
    licznik+=1
    
    if liczba==0:
        zera+=1
    elif liczba%2==0 and liczba!=0:
        parzyste+=1
    else:
        nieparzyste+=1


if parzyste==20:
    print("Parzyste pierwsze!")
elif nieparzyste==20:
    print("Nieparzyste pierwsze!")

print("Wylosowanych zer:", zera, ". Wylosowanych liczb parzystych:", \
      parzyste,". Wylosowanych liczb nieparzystych:", nieparzyste, \
      ". Łącznie było trzeba tylu losowań:", licznik)


haslo=input("Podaj hasło\n")
proba=""
licznik=3
while proba!=haslo and licznik!=0: #zatrzyma się tylko, gdy podamy 3 błędne hasła i czwarte poprawne, musi być AND
    proba=input("Zgadnij hasło\n")
    if proba!=haslo:
        licznik-=1
            


