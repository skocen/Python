x=int(input("Upisi dimenziju matrice:"))
a=[[0 for row in range(0,x)] for col in range(0,x)]
p=q=m=n=int(0)
for i in range (0,x):
  for j in range (0,x):
    print ("Upisi broj:")
    a[i][j]=int(input())
    if(i==0 and j==0):
          maks=a[i][j]
          mini=a[i][j]
    if(a[i][j]>maks):
          maks=a[i][j]
          q=i
          p=j
    if(a[i][j]<mini):
          mini=a[i][j]
          m=i
          n=j
print("Matrica:",a)
print("Maksimalan:",maks,"[",q,"][",p,"]")
print("Minimalan:",mini,"[",m,"][",n,"]")

