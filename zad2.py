a=int(input('Unesi prvi broj: '))
b=int(input('Unesi drugi broj: '))
c=[0,0,0,0,0,0,0,0,0,0]
while(a>0):
    if(c[a%10]==0):
        c[a%10]=1
    a=a//10
while(b>0):
    if(c[b%10]==0):
        c[b%10]=1
    b=b//10
for j in range(0,len(c)):
    if(c[j]==1):
        print(j,end=" ")
