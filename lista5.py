  n=int(input("unesi broj brojeva :"))
b=[]
c=[]
for i in range(n):
    a=int(input("unesi broj :"))
    b.append(a)
    if (b[i]>0):
        c.append(b[i])
print("ispis liste")
for i in range(len(b)):
     print(b[i],end=" ")
print()
print("ispis pozitivnih")
for i in range(len(c)):
    print(c[i],end=" ")
