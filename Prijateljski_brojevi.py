k=100
while k<=999 : #provjerava redom brojeve od 100 do 999 imaju li prijateljski par
    s=0 #zbroj djelitelja od k
    for i in range (1,k,1) :  #računa zbroj djelitelja od broja k
        if (k%i)==0 :
            s+=i
    k1=0 #zbroj djelitelja od s
    for i in range (1,s,1) :  #računa zbroj djelitelja od broja s
        if (s%i)==0 :
            k1+=i
    if k1==k : #provjerava je li zbroj djelitelja od s jednak broju k
        print('Prijateljski par = ({},{})'.format(k,s))
    k+=1
