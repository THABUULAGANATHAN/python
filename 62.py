bht=str(input())
lact=[]
tint=""
rest=0
for i in range(0,len(bht)):
    for j in range(i,len(bht)):
        tint=tint+bht[j]
        if(tint[::-1]==tint):
            rest=len(bht)-len(tint)
            lact.append(rest)
    tint=""
print(min(lact))
