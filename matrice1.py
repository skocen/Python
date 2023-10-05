n=int(11)
while (n>10):
    n=int(input("Upisi dimenziju matrice:"))
a=[[0 for row in range(n)] for col in range(n)]
for i in range (n):
  for j in range (n):
    print ("Upisi broj:")
    a[i][j]=int(input())
print("Matrica:",a)
r=int(input("Upisi broj retka:"))
s=int(0)
for i in range(n):
    s+=a[r][i]
print("Suma=",s)

