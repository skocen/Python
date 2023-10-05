'''

ZADATAK: unos N brojeva u listu, ispis sortirano
'''
# unosimo podatak koliko brojeva ćemo stavljati u listu
N=int(input())
# obavezno prije korištenja definiramo listu
B=list()
# radimo petlju koja će se N puta ponavljati
for i in range(N):
    # u svakom krugu petlje unosimo neki broj u "pomoćnu varijablu" A
    A=int(input())
    # dodavanje u listu B
    B.append(A)
# sortiranje liste
B.sort()
# ispišimo listu u jednom redu odvojeno zvjezdicama
for i in B:
    print(i,end="*")
print()
print("malo kvalitetniji ispis")

for i in range(len(B)):
    # ispiši ali neidi u drugi red
    print(B[i],end="")
    # ako se ne radi o zadnjem elementu ispiši *
    if i!=len(B)-1:
        print("*",end="")
print()
# mogu napraviti i svoj vlastiti string
D=""
for i in range(len(B)):#
    # u D string (na)dodajem broj B[i] koji sa str() pretvaram u string
    D+=str(B[i])
    # ako se ne radi o zadnjem elementu ispiši *
    if i!=len(B)-1:
        D+="*"
# mogu ispisati string D
print("D string =",D)
