mojaLista = [1, 2, 100, 200, 5, 6]
print('moja lista',mojaLista)
print('Elementi na neparnim indeksima', mojaLista[::2])
print('Elementi na parnim indeksima', mojaLista[1::2])
# Najčešća primjena negativnog indeksa - okretanje liste
print('Okrenuta lista', mojaLista[::-1])

# Dodjeljivanje također radi ...
mojaLista[::2] = [0, 0, 0]
print('Dodjela neparnim indeksima', mojaLista)

# ... ali samo kad nova lista ima isto elemenata koliko i isječak
#mojaLista[1::2] = [0]

'''
[::]
početak isječka i njegov kraj.
Onaj treći nam govori da li uzimamo svaki element, svaki drugi, svaki peti i slično. Ako se ne navede on,
 ili se izostavi druga dvotočka,
 podrazumijeva se da je njegova vrijednost 1.
 '''






