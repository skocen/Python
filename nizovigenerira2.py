from random import*
n=int(input('Unesi broj: '))
a=list()
b=list()
s=int(0)
for i in range(n):
    a.append(randint(1,100))
print('Početni niz: ')
for i in range(len(a)):
    print(a[i],end= ' ')
for j in range(n):
    for i in range(j+1):
        s=s+a[i]
    b.append(s)
    s=int(0)
print('\n Konačni niz: ')
for i in range(len(b)):
     print(b[i],end= ' ')
a.sort()
print('\n Početni niz sortirani: ')
for i in range(len(a)):
    print(a[i],end= ' ')

