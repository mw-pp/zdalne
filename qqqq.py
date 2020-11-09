





haslo=input("Podaj hasło\n")
proba=""
licznik=3

while proba!=haslo and  licznik!=0:
    proba=input("Zgadnij hasło\n")
    if proba!=haslo:
        licznik-=1







##licznik=0
####while licznik<100:
####    print("JEDEN. hej")
##
##while licznik>100:
##    print("DWA. hej")
##
##while licznik!=10:
##    print("TRZY. hej")
##    licznik+=1






























##import time, random
##
##litery="abcdefghij"
##
##### liczniki
##powtorzenia=int(input("Ile chcesz powtórzeń?\n"))
##odpP=0
##odpF=0
##
##### czasy reakcji
##sumaCzasow=0
##sumaP=0
##sumaF=0
##
##for i in range (powtorzenia):
##    los=random.choice(litery)
##    print("Naduś", los)
##    start=time.time()
##    odp=input()
##    koniec=time.time()
##    rt=koniec-start
##    
##    if odp==los:
##        print("Dobrze")
##        odpP+=1
##        sumaP+=rt
##    else:
##        print("Źle")
##        odpF+=1
##        sumaF+=rt
##
##    print(round(rt, 2))
##    sumaCzasow+=rt
##print("Pawidłowych odpowiedzi było", odpP, "a nieprawidłowych", odpF)
##
##srednia=sumaCzasow/powtorzenia
##sredniaP=sumaP/odpP
##sredniaF=sumaF/odpF
##print("Średni czas reakcji to", round(srednia,2), \
##      ". Średni czas reakcji prawdiłowych to", round(sredniaP,2),\
##      "Średni czas reakcji nieprawidłowych to", round(sredniaF,2))
##









