d=s=int(0)
while(1):
    a=int(input("Unesi broj:"))
    for i in range (1,a):
        if(a%i==0):
            d+=1
    if(d==1):
        while(a>0):
            s+=a%10
            a//=10
        print("Zbroj znamenki unesenog prostog broja je ",s)
        break;
    else:
        d=0

