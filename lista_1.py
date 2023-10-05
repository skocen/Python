'''
Osnove o listama
'''
A=[] # prazna lista - ili A=list()
B=[1, 5, 22, 8, 9]  # pridruživanje 5 brojeva iz liste
# možemo promijeniti vrijednost elementa iz liste
B[3]=1000
A.append(23)    # dodali smo broj 23 na kraj liste A
B.append(23)    # dodali smo broj 23 na kraj liste B
print("A",A)    # ispis liste A - ne vide se i uglate zagrade
print("B",B)
# slobodno se miješaju tipovi podataka u listama (nizovima)
A.append("Marko")
print("A",A)
# ispis prvog elemnta liste A
print("prvi element liste A",A[0])
# ispis svih elemenata iz liste B radimo PETLJOM FOR
print("ispis svih elemenata liste B, jedan po jedan")
for i in range(len(B)): # len(B) daje broj elemenata u listi - kod nas je to 6
    # i je indeks elementa
    # B[i] uzima vrijednost i-tog elementa iz B liste
    print(str(i)+". - ",B[i])
print("ispis bez indeksa")
# za svaki krug petlje u i stavi redosljedno element
for i in B:
    print(i)
