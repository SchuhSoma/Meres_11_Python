print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Meseorszag_Soma")
EladoNeveTMb=["Hófehérke", "Csipkerózsika","Herceg","Mostoha","Morgó","Hamupipőke","Vadász"]
HiredettArTM=[52.6,32.7,64.2,48.5,22.3,55.7,28.4]
import random
IngatlaMereteTMB=[]
for i in range(7):
    IngatlaMereteTMB.append(random.randint(43,67)) 
    
for i in range(len(EladoNeveTMb)):
    print("\t ",EladoNeveTMb[i],":\t ",HiredettArTM[i],"MFt\t ",IngatlaMereteTMB[i],"nM")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
Osszbevetel=0
for i in range(len(HiredettArTM)):
    Osszbevetel+=HiredettArTM[i];
print("A várható össz bevétel: ",Osszbevetel,"MFt")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
db55=0
for i in range(len(IngatlaMereteTMB)):
    if(IngatlaMereteTMB[i]>55):
        db55+=1
print("Ennyi esetben volt az ingatlan mérete 55nM feletti: ",db55)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
import sys
MinMeret=sys.maxsize
MinElado=""
for i in range(len(IngatlaMereteTMB)):
    if(MinMeret>IngatlaMereteTMB[i]):
        MinMeret=IngatlaMereteTMB[i]
        MinElado=EladoNeveTMb[i]
print("A legkkisebb ingatlan mérete: ",MinMeret,"\t eladó neve: ",MinElado)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
Keresett="Herceg"
Szamlalo=0
while Szamlalo<len(IngatlaMereteTMB) and EladoNeveTMb[Szamlalo]!=Keresett:
    Szamlalo+=1
if(Szamlalo==len(IngatlaMereteTMB)):
    print("Nincs ilyen igatlan")
else:
    print("Herceg inhatlanjának mérete: ",IngatlaMereteTMB[Szamlalo]," nM Ingatlan eladási ára: ",HiredettArTM[Szamlalo]," MFt")
print("\n--------------------------------------------------------------------------\n")
print("Veletlenek_Soma")
Hossz=input("Kérem adja meg hány elemet szeretne generálni: ")
N=int(Hossz)
Ertek1=input("Kérem adja meg a legkisebb érteket: ")
Min=int(Ertek1)
Ertek2=input("Kérem adja meg a legnagyobb értéket: ")
Max=int(Ertek2)
GeneraltList=[]
for i in range(N):
    GeneraltList.append(random.randint(Min, Max))
for i in range(len(GeneraltList)):
    print("\t",i,"\t",GeneraltList[i])
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
Szamlalo2=0
while Szamlalo2<len(GeneraltList) and GeneraltList[Szamlalo2]%15!=0:
    Szamlalo2+=1
if(Szamlalo2==len(GeneraltList)):
    print("Nincs ilyen elem a listában ami osztható 15-el")
else:
    print("A lista ennyiedik eleme :",Szamlalo2+1,"eleme osztható 15-el")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
ParatlanList=[]
for i in range(len(GeneraltList)):
    if(GeneraltList[i]%2==1):
        ParatlanList.append(GeneraltList[i])
for i in range(len(ParatlanList)):
    print(ParatlanList[i])
