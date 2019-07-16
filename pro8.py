import math
ct22,l23=map(int,input().split())
mt25=[]
kt12=list(map(int,input().split()))
for j in range(0,l23):
    pt12,qt32=map(int,input().split())
    mt25.append([pt12,qt32])
for j in mt25:
    xt23=j[0]-1
    yt24=j[1]-1
    print(math.gcd(kt12[xt23],kt12[yt24]))
