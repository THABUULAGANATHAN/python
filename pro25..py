sst3=input()
min3=len(sst3)
i=0
while(i<min3):
    mt3=0
    kt3=0
    for j in range(len(sst3)):
        kt3+=1
        if(sst3[i]==sst3[j]):
            if(kt3>mt3):
                mt3=kt3
            kt3=0
        if(kt3>min3):
            break
    if(kt3>mt3):
        mt3=kt3
    if(mt3<min3):
        min3=mt3
    i+=1
print(min3)
