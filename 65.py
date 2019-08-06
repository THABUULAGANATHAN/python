bht,jst=map(int,input().split())
lisat=list(map(int,input().split()))[:bht]
rant=int(input())
surt=(sum(lisat)-lisat[jst])//2
if (surt==rant):
    print("Bon Appetit")
else:
    print(abst(surt-rant))
