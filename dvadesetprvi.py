a = []
b = []
q = 0
while q<50:
    x = int(input('Unesi broj: '))
    if x==-1:
        break
    a.append(x)
    q = q + 1
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
for i in range(len(b)):
    print(b[i], end=' ')
