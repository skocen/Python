a,b=map(int, input("Upisi dva broja odvojena razmakom:").split())
if a>b:
    kv=int(a*a)
    zn=chr(a)
    print("Prvi broj je veci. Broj:",a,"Znak:",zn,"Kvadrat:",kv)
elif b>a:
    zn=chr(b)
    s=a+b
    print("Drugi broj je veci. Broj:",b,"Znak:",zn,"Suma:",s)
else:
    print("Brojevi su jednaki")
