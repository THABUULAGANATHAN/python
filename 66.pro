bht, spt, jst, kimt = map(int, input().split())
sst= 0
dakt = spt-jst
if (dakt >= 0):
    setc = (bht-jst)*2
    for i in range (kimt):
        if (i == kimt-1):
             sect =sect/ 2
        if (dakt < sect):
            dakt= spt
            sst += 1
        dakt = dakt - sect
        if (dakt < 0):
            sst = -1
            break
        sect = 2*bht - sect
    print (sst)
else:
    print (-1)
