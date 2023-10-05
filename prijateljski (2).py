for i in range (100,1000):
    s = int (0)
    if (i%50==0):
        print ("...")
    for z in range (1,i):
        if (i%z)==0:
            s+=z
    for j in range (100, 1000):
        q= int (0)
        for e in range (1, j):
            if (j%e)==0:
                q+=e
        if (s==j) and (i==q):
            print (i, "¤¤¤ ",j)
print ("Kraj programa")
