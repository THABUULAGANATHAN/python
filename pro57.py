ptt,qrt=map(str,input().split())
ct=0
for i in range(0,len(ptt)):
    for j in range(0,len(qrt)):
        if ptt[i]==qrt[j]:
            ct+=1
if ct>=2:
    print("yes")
else:
    print("no")
