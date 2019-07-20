nummt=int(input())
aat=list(map(int,input().split()))
pt=[]
qt=[]
for i in range(len(aat)):
	if i%2==0:
		pt.append(aat[i])
	else:
		qt.append(aat[i])
st=sum(pt)
rt=sum(qt)
if(st>rt):
	print(st)
else:
	print(rt)
