m=n=int(6)
while (n>5 or m>5):
    n,m=map(int,input("Upisi dimnezije matrice odvojene razmakom:").split())
a=[[0 for row in range(n)] for col in range(m)]
for i in range (n):
  for j in range (m):
    print ("Upisi broj:")
    a[i][j]=int(input())
print("Matrica:",a)
s=int(input("Upisi broj stupca:"))
p=int(1)
for i in range(n):
    s*=a[i][s]
print("Produkt=",s)
