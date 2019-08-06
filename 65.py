bht,jst=map(int,input().split())
lisat=list(map(int,input().split()))[:bht]
ran=int(input())
surt=(sum(lisat)-lisat[jst])//2
if (surt==ran):
    print("Bon Appetit")
else:
    print(abst(surt-ran))
