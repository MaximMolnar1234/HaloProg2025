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

# 4. Van-e 0 pontos versenyző? (Eldöntés 1)
j=1
while j<len(verseny_adatok) and int(verseny_adatok[j].split(",")[1])>0:
    j+=1
if (j<len(verseny_adatok)):
    print("Van 0 pontos versenyző.")
else: 
    print("Nincs 0 pontos versenyző.")    
# 4.2 Mindeki szerzett már pontot?  (Eldöntés 2)      

k=1
while k<len(verseny_adatok) and int(verseny_adatok[k].split(",")[1])>0:
    k+=1
if (k>=len(verseny_adatok)):
    print("Mindenki szerzett pontot.")
else:
    print("Van olyan aki nem szerzett pontot.")       


# 5. Ki vezeti a tabellát? (Maximumkiválasztás)
max_ertek = int(verseny_adatok[1].split(",")[1])
max_index = 1
for i in range(2,len(verseny_adatok)):
    if (int(verseny_adatok[i].split(",")[1]))>max_ertek:
        max_index = i
        max_ertek = int(verseny_adatok[i].split(",")[1])
print(f"Ő vezet: {verseny_adatok[max_index].split(",")[0]}") 
       


# 6. Ki az aki 90 pontot szerzett? Keresés (lineráris)

l=1

while l<len(verseny_adatok) and int(verseny_adatok[l].split(",")[1]) !=90:
    l+=1
    
if (l<len(verseny_adatok)):
    print("A 90 pontos versenyző neve: ",verseny_adatok[l].split(",")[0])    
else:
    print("A fájlban nincs olyan versenyző akinek pontosan 90 pontja van")

# 7. Kik a Mercedes versenyzői?

lista = []


db2=0
for i in range (1, len(verseny_adatok)):
    if (verseny_adatok[i].split(",")[2] == "Mercedes"):
        lista[db2]=verseny_adatok[i].split(",")[1]
        db2+=1
print(lista)


print("ITT A VÉGE!")    








#fajl_tartalom = fajl.read()
#fajl_tartalom1 = fajl.read(111)


#print(fajl_tartalom)
#print(f"\n\n{fajl_tartalom1}")

#fajl_tartalom2 = []

#fajl_tartalom2 = fajl.readlines()

#print(len(fajl_tartalom2))


#fajl.close()