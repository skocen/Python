from random import*
from math import*
n,m,x=map(int, input("Upisi granice intervala i broj brojeva:").split())
for i in range(0,x):
    a=int(randint(n,m))
    print("Broj:{} Kvadrat:{} Korijen:{:.2f}".format(a,a*a,sqrt(a)))
