ntn11,ntn21=list(map(int,input().split()))
lit1=list(map(int,input().split()))
lit2=[]
while(ntn21):
	kt = list(map(int,input().split()))
	lit2.append(kt)
	ntn21-=1
for ic in lit2:
	val=0
	for jc in range(ic[0]-1,ic[1]):
		val=val^lit1[jc]
	print(val)
