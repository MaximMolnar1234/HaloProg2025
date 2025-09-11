import random

#Lista létrehozása
szamok = []
#Lista feltöltése 100 db random kétjegyű egész számmal
for i in range(100):
    szam = random.randint(10, 99)
    szamok.append(szam)
#Ellenőrizni
print(szamok)
print(len(szamok)) 

# EGYSZÁM JÁTÉK
jatek_szam = 0
nem_talalDB = 0
kitalalando_szam = szamok[random.randint(0, len(szamok))]

#Játék

jatszol = True

while (jatszol):
  tipp=int(input("Tipped?: (egész szám)"))
  
  while (tipp != kitalalando_szam):
        tipp=int(input("Tipped?: (egész szám)"))
        
  print("Eltaláltad a számot!")  

  folytatas = input("Akarsz-e még játszani? [I/N]")
  if (folytatas == "N"):
      jatszol = False
      
      



""" tipp=int(input("Tipped?: (egész szám)"))
while (tipp != kitalalando_szam):
    tipp=int(input("Tipped?: (egész szám)"))
print("Eltaláltad a számot!")

folytatas = input("Akarsz-e még játszani? [I/N]")

if (folytatas == "I"):
    #??????????
    pass
else:
    exit()  """
    
    
          
            