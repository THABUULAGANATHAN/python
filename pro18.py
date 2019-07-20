aprt,brt=map(int,input().split())
l1t=[]
for _ in range(aprt):
    l1t.append(input())
for ic in range(len(l1t)):
    if('0' in l1t[ic]):
        l1t[ic]=l1t[ic].replace('0','')
    l1t[ic]=l1t[ic].replace(' ','')
lengths=[]
for ic in l1t:
    if(len(ic)>0):
        lengths.append(len(ic))
brt=min(lengths)
rt1='1 '*brt
rt1=rt1.strip()
for ic in range(brt):
    print(rt1)
