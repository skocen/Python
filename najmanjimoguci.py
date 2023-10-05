from math import*
x=int(input("Upisi pozitivni cijeli broj:"))
u=x*x
for i in range (1,int(log(x,10)+1)):
    a=x//(10**i)
    b=x%(10**i)
    if(a*b<u):
        u=a*b
        m,n=a,b
print(m,n)
