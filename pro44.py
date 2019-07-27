bt1,bt2,bt3,bt4=map(int,input().split())
liss=list(map(int,input().split()))
xen=[]
for i in range(0,len(liss)):
    for j in range(i,len(liss)):
        for k in range(j,len(liss)):
            xen.append(bt2*liss[i]+bt3*liss[j]+bt4*liss[k])
print(max(xen))
