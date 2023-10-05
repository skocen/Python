from random import*
n=int(11)
while (n>10):
    n=int(input("Upisi dimenziju matrice:"))
a=[[0 for row in range(n)] for col in range(n)]
s=[0 for row in range(n)]
for i in range (n):
  for j in range (n):
    a[i][j]=float((randint(0,90))/100)
print("Matrica:",a)
for i in range (n):
  for j in range (n):
      s[i]+=a[i][j]
for i in range(n):
    s[i]/=n
print("Aritmeticke sredine po redovima:",s)
for i in range(n):
   if(i==0):
        maks=float(s[i])
        ind=0
   if(s[i]>maks):
         maks=s[i]
         ind=i
print("Najveca aritmeticka sredina je u ",ind+1,". retku")
