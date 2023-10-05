A=[1, 5, 22, 8, 9]
for i in A[1:3]:
    print(i)
# vrijedi "sliceing od do" kao i kod stringova
# stvaranje nove liste B
B=[]
# dodavanje liste A u listu B - tzv dvodimenzinalna lista
B.append(A)
# još jedno dodavanje
B.append(A)
# ispis
print(B)
# promjena prve (nulte) vrijenosti liste A
A[0]=555
print(A)
print(B)
# VAŽNO: u listi B nalaze se 2 liste A, a ne vrijenosti
# stoga promjenom liste A, promijenjen je i sadržaj liste B koja
# No, kako duplicirati vrijenosti listi???
C=[]
C.extend(A)
C.extend(A)
A[0]=9999
print(A)
print(C)
# lista C s extend dobila je vrijednosti i nema nikakve povezanosti s listom A
# listi c su se sa extend nadodale vrijednosti elemeneta
# kako stvoriti dvodimenzinalnu listu ??? npr. 2 reda i 3 stupca
# primjer 1.
D=[[1,2,3],[4,5,6]]
print("lista D",D)
# primjer 2.
E=[]
E.append([1,2,3])
E.append([4,5,6])
print("lista E",E)
# primjer 3.
F=[1,2,3]
G=[4,5,6]
H=[]
# želimo dodati listu F i G, ali da nema povezane vrijednosti
# stoga ćemo H listu proširiti
# kako extend samo uzima vrijednosti, stavit ćemo to u listu
H.extend([F]) # listu F smo stavili u uglate zagrade
H.extend([G]) # listu G smo stavili u uglate zagrade
print("lista H:",H)
# mijenjamo li listu H ili G, neće se mijenjati vrijenosti u listi H
# no, da smo dodali liste s APPEND, tada bismo imali povezane liste što uglavnom NE ŽELIMO
# kako ispisati liste
for i in H: # iz liste H vadi elemente, a elementi su 2 liste: [1, 2, 3] i [4, 5, 6]
    print(i)  # ispisuje jednu po jednu listu
# kako ispisati sve elemente bez uglatih zagrada ?
for i in H: # iz liste H vadi elemente, a elementi su 2 liste: [1, 2, 3] i [4, 5, 6]
    for j in i: # sada iz liste i uzima svaki element i stavlja ga u j
        print(j,end=" ")  # ispisuje po jedan element - j
    print() # samo da ode u drugi red
# direktno dohvaćanje nekog elementa - npr H[1,2]
print("H[1,2] = ",H[1][2]) # H[1]=[4, 5, 6] pa je drugi element = broj 6
# kako sortirati listu koja je dvodimenzinalna?
# sortiramo naopačke liste [1, 2, 3] i [4, 5, 6] koje su cjelina unutar liste H
H.sort(key=lambda x:x[2], reverse=True)
print("obrnuto sortirana lista H:",H)
# VAŽNO
# na ovaj način možemo imati svašta unutar jedne liste te sortirati  je kako želimo
# primjer: unsesi ime učenike, godine i visinu
# ispiši ih prvo po imenu, pa po godinama te visini
# nećemo unositi, već napraviti listu
K=[["Pero",12,128.3],["Ana",14,144.8],["Ivana",10,133.2]]
# sortirat ću ih po imenu
K.sort(key=lambda x:x[0])
print("sortirani po imenu:",K)
# sortirat ću ih po godinama
K.sort(key=lambda x:x[1])
print("sortirani po godinama:",K)
# sortirat ću ih po visini
K.sort(key=lambda x:x[2],reverse=True)
print("sortirani po visini obrnuto:",K)
# VAŽNO: unutarnje liste se drže ZAJEDNO
# to su tzv. slogovi ili zapisi (engl. records)
# o tome kada jednog dana upoznate rad s bazama podataka... :-)
