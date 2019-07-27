import sys, string, math

nunt = 4
Laat = []
for i in range(0,nunt) :
    Laat.append([])
Lt2 = []
for i in range(0,nunt) :
   Laat[i] = [ int(x) for x in input().split()]
xt1 = Laat[0][0]
yt1 = Laat[0][1]
for i in range(1,nunt) :
    if Laat[i][0] != xt1 and Laat[i][1] != yt1 :
        xt3 = Laat[i][0]
        yt3 = Laat[i][1]
        i2 = i
        break

Lt3 = [0,i2]
for i in range(1,nunt) :
    if i != i2  :
        xt2 = Laat[i][0]
        yt2 = Laat[i][1]
        Lt3.append(i)
        break
for i in range(1,nunt) :
    if i not in Lt3  :
        xt4 = Laat[i][0]
        yt4 = Laat[i][1]
        Lt3.append(i)
        break

if xt1==xt2 :
    if yt2==yt3 and xt4==xt3 and yt4==yt1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
elif xt1==xt4 :
    if yt4==yt3 and xt2==xt3 and yt2==yt1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
