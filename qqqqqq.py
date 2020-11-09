import random

for i in range(5):
    
  
    los=random.randint(1,16)
    if los==5 or los==9 or los==10:
        
        print(los, "Zajęte")
        continue

    print(los)

##for y in range(5):
##    los=random.randint(2,5)
##    if los==3 or los==4:
##        print(los, "Zajęte") #pass
##    else:
##        print(los)
