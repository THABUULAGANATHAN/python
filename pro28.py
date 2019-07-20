arrt=int(input())
brrt=[int(st) for st in input().split()]
brrt.sort()
st=0
xvt=0
for i in range(len(brrt)):
    if brrt[i]>=st:
        xvt+=1
    st=st+brrt[i]
print(xvt)
