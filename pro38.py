nint,kint=map(int,input().split())
Lt=list(map(int,input().split()))
Ct=0
for Xt in Lt:
    if Xt<=(5-kint):
        Ct+=1
Gt=Ct//3
print(Gt)
