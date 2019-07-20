Pt = int(input())
Qt = [ int(i) for i in input().split()]
Pt = len(Qt)
Ut = 0
for Xt in range(0,Pt-2):
    for Yt in range(Xt+1, Pt-1):
        for Zt in range(Yt+1, Pt):
            if Qt[Xt] > Qt[Yt] > Qt[Zt] :
                Ut =Ut+ 1
print(Ut)
