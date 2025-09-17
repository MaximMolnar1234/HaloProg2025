"""----------------------------------------------
    EGYSZÁM JÁTÉK
----------------------------------------------"""

import random


# Lista létrehozása
szamok = []

# Kitalálandó számok listájának feltöltése 40 db, random kétjegyű egész számmal
while len(szamok) !=40:
    szam = random.randint(10, 99)
    
    if (szam not in szamok):
        szamok.append(szam)

    

# Ellenőrzés
print(szamok)


# Változók létrehozása statisztika készítéshez
jatek_szam = 1
nem_talaltdDB = 0

# A kitalálandó szám kiválasztása a listából
kitalalando_szam = szamok[random.randint(0, len(szamok))]


# A JÁTÉK ---------------------------------------
kitalalando_szam = 12

jatszol = True

while(jatszol):
    
        
    tipp_sz = input("Tipped? (egész szám): ").strip()
    if(tipp_sz.isdecimal()):
        tipp = int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        continue

    while(tipp != kitalalando_szam):
        nem_talaltdDB += 1
        
        if (tipp == 123):
            pass
        elif (tipp < kitalalando_szam):
            print("A kitalálandó szám nagyobb!")
            nem_talaltdDB += 1
        elif(tipp > kitalalando_szam):
            print("A kitalálandó szám kisebb!")
            nem_talaltdDB += 1
               
        tipp_sz = input("Tipped? (egész szám)\n Kilépés \'X\' karakterrel: ").strip()
        
        if(tipp_sz.isdecimal()):
            tipp = int(tipp_sz)
        elif tipp_sz == 'X' or tipp_sz == 'x':
            print(f"\nJátékok száma: {jatek_szam} Próbálkozások száma: {nem_talaltdDB}")
            exit()    
        else:
            print("Egész számmal játsz!")
            tipp = 123
            continue

    print("Kitaláltad a kitalálandó számot!")

    folytatas = input("Akarsz-e még játszani? [I/N]")
    
    if(folytatas == "N"):
        jatszol = False
        print(f"\nJátékok száma: {jatek_szam} Próbálkozások száma: {nem_talaltdDB}")
    elif(folytatas == "I"): 
        jatek_szam+=1    

          
            