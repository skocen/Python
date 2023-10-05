'''
rad s listama
'''
A=['Vito', 'Goran', 'Marin']
# ispis prvog elementa
print(A[0])
# ispis svih
print(A)
# ispis prva 2, od početka do drugog
print(A[:2])
# ispis od drugog (uključen i on) elementa do kraja
print(A[1:])
# ispis zadnjeg - A[2]
print(A[-1])
# metode LISTE
# dodavanje elementa
A.append(3) # dodaje broj
print(A)
A.append(input('unesi nešto: ')) # dodaje string na kraj
print(A)
A[len(A)-1]=22 # len(A) - vraća broj elemenata liste
# ispis elemenata - 1. način
print('ispis elemenata niza - putem vrijednosti')
for i in A: # svaki element iz A, jedan po jedan u svakom krugu petlje, stavlja u I
    print(i) # u svakom krugu petlje ispisujem vrijednost I
# ispis elemenata - 2. način - pomoću indeksa
print('ispis elemenata niza - putem indeksa')
for i in range(len(A)): # u varijablu I svaki put se uzima po jedna broj iz ranga
    print(A[i]) # ispisujem element A koji ima indeks I
# metode LISTE
print('broj elemenata 22 u A =',A.count(22)) # daje koliko ima elemenata s vrijednošću 22
A.insert(3,55) # na treće mjesto (indeks) umeće broj 55
print(A)
for i in range(len(A)): # u varijablu I svaki put se uzima po jedna broj iz ranga
    print(str(i)+'.',A[i]) # ispisujem element A koji ima indeks I
A.pop(1) # briše 1 element (po indeksu),
# del A[1] # isto kao i prethodna naredba
print('indeks vrijednosti elementa 55:',A.index(55)) # pronalazi indeks prvog elementa po vrijednosti
A.sort() # sortira elemente po vrijednosti uzlazno ili - sorted(A)
print(A)
A.reverse() # sortira elemente po vrijednosti obrnuto ili reversed(A)
print(A)
A.clear() # briše sve elemente liste
print(A)
