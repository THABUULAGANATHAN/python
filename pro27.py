Aat1,Bbt=map(int,input().split())
Cct=list(map(int,input().split()))
prt=list(map(int,input().split()))
qrt=[]
art=0
for i in range(Aat1):
    xt=prt[i]/Cct[i]
    qrt.append(xt)
while Bbt>=0 and len(qrt)>0:
    mindex=qrt.index(max(qrt))
    if Bbt>=Cct[mindex]:
        art=art+prt[mindex]
        Bbt=Bbt-Cct[mindex]
    Cct.pop(mindex)
    prt.pop(mindex)
    qrt.pop(mindex)
print(art)
