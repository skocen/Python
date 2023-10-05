b=[]
c=[]

while(1):
    a=int(input('Unesi broj:'))
    if a!=-1:
        b.append(a)
    else:
        break;
b.append(100000000000000)
dj=int(1)
for i in range(0,len(b)):
    if i>0:
        if b[i]==b[i-1]:
            dj=dj+1
        else:
            c.append(b[i-1])
            c.append(dj)
            dj=1

print('Ispis niza:')
for i in range(len(b)-1):
        print(b[i])

print('Ispis komprimiranog niza:')
for i in range(len(c)):
        print(c[i])
