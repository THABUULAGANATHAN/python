bt=str(input())
st=str(input())
sst=""
tat1=0
tat2=0
tst=""
rst=""
for i in range(0,len(bt)):
    tat1=ord(bt[i])-96
    tat2=ord(st[i])+tat1
    if(tat2>122):
        tat2=tat2-122
        tat2=tat2+96
    tst=tst+chr(tat2)
print(tst)
