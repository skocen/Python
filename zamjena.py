# Zamjena je iste dužine
mojaLista = [1, 2, 100, 200, 5, 6]
mojaLista[2:4] = [3, 4]
print('Zamjena iste dužine', mojaLista)

# Zamjena je kraća
mojaLista = [1, 2, 100, 200, 5, 6]
mojaLista[2:4] = []
print('Zamjena kraćom listom', mojaLista)

# Zamjena je duža
mojaLista = [1, 2, 100, 200, 5, 6]
mojaLista[2:4] = [3, 3.25, 3.5, 3.75, 4]
print('Zamjena dužom listom', mojaLista)

