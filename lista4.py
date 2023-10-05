n=int(input("unesi broj brojeva :"))# unosimo podatak koliko brojeva ćemo stavljati u listu
b=list()#definiramo listu ili  b=[]
for i in range(n):
    a=int(input("unesi broj :"))# u svakom krugu petlje unosimo neki broj u "pomoćnu varijablu" a
    b.append(a) # dodavanje u listu b
for i in b:
    print(i,end="*")# ispišimo listu u jednom redu odvojeno zvjezdicama
print()
print(" ispis s razmakom")
for i in range(len(b)):
        print(b[i],end=" ")# ispiši ali neidi u drugi red
print()
for i in range(len(b)):#ispis s indeksom
    print(b[i],"[",i,"]",sep="")
