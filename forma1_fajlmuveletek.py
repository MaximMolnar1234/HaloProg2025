#import io

verseny_adatok = []


try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        
        for sor in fajl:
            verseny_adatok.append(sor)

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

print(verseny_adatok)
"""
    1. Sorozatszámítás/összegzés
    2. Kiválasztás
    3. Megszámlálás
    4. Eldöntés 1, 2
    5. Maximum/ minimum kiválasztás
    6. Keresés (lineráris)
    
    
    . Kiválasztás
    . Szétválogatás
    . Rendezés
    . Unió
    . Metszet
    
    .Rendezés
        -egyszerű cserés
        -buborékos
        -minumumkiválasztásos
        -beszúró

"""
# 1. Mennyi egy pontszám átlag?
pontszam = 0
db = len(verseny_adatok)-1

for i in range (1,len(verseny_adatok)):
    sor = verseny_adatok[i].split(",")
    pontszam = pontszam+int(sor[1])
    
print("Ennyi a pontszámok átlga: ",pontszam/db)

# 2.  Mik a bekért versenyző adatai?
versenyzo = input("Adj meg egy versenyzőnevet: ")

i=1
while (verseny_adatok[i].split(",")[0]!=versenyzo):
    i=i+1
print(verseny_adatok[i])

# 3. Hány versenyző teljesített 300 pont felett?

db_300_felett=0
for i in range (1,len(verseny_adatok)):
    if (int(verseny_adatok[i].split(",")[1])>300):
        db_300_felett+=1
print(f"A 300 pont feletti versenyzők száma: {db_300_felett} fő")        

# 4. Van-e 0 pontos versenyző?
j=0
while ():




print("ITT A VÉGE!")    








#fajl_tartalom = fajl.read()
#fajl_tartalom1 = fajl.read(111)


#print(fajl_tartalom)
#print(f"\n\n{fajl_tartalom1}")

#fajl_tartalom2 = []

#fajl_tartalom2 = fajl.readlines()

#print(len(fajl_tartalom2))


#fajl.close()