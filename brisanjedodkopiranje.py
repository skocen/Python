pocetnaLista = [14, 8, 7, 12, 11]
print('Prva dva elementa', pocetnaLista[:2])
print('Poslednja dva elementa', pocetnaLista[-2:])
# Kopiraj listu
kopijaListe = pocetnaLista[:]
# Obriši poslednji
del kopijaListe[-1]
print('Original', pocetnaLista)
print('Izmjenjena', kopijaListe)
del pocetnaLista[-1] # Element na kraju
del pocetnaLista[2]  # Element na poziciji 2
print('Nakon brisanja:', pocetnaLista)
# Ovde ne možemo pretjerati sa indeksima:
# Ako je indeks prevelik, element se dodaje na kraj
# Ako je indeks previše malen, element se dodaje na početak
pocetnaLista.insert(200, 'ja sam na kraju')
pocetnaLista.insert(-50, 'ja sam na pocetku')
print('Konačna lista', pocetnaLista)
print('Prva tri elementa', pocetnaLista[0:3])
print('Svi elementi osim poslednjeg', pocetnaLista[0:-1])
# Iako je rezultat samo jedan element, sječenje vraća niz!
print('Samo prvi element', pocetnaLista[0:1])
# Ili nekad prazan
print('Nepostojeći isječak', pocetnaLista[100:120])




