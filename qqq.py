import random

liczba=0
while liczba!=5:
    los=random.randint(1,2)
    print("Wszystkie", los)
    if not los==2:
        liczba+=1
        print("trafiony")
 
