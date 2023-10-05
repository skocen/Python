from random import*

n=int(input('Unesi n: '))
a=list()
b=list()
s=0
for i in range(n):
    x=randint(1,100)
    a.append(x)
    s=s+x
    b.append(s)

b.sort()
a.sort()

for j in range(len(a)):
    print(a[j],end=" ")

print("\n")
for k in range(len(b)):
    print(b[k],end=" ")

