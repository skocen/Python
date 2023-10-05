b=int(input("Upisi broj u binarnom sistemu:"))
d=int(0)
a=int(1)
while(b>0):
    d+=b%10*a
    a*=2
    b//=10
print("Broj u dekadnom sistemu:",d)
