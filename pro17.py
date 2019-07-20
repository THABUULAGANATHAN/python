npit=input()
at1=list(map(int,npit.split()))
kt1=at1[1]
ht=input()
flag1=0
svt=list(map(int,ht.split()))
for i in range(0,len(svt)-1):
	for j in range(i+1,len(svt)):
		if svt[i]+svt[j]==kt1:
			print("yes")
			flag1=1
			break
	if flag1==1:
		break
if flag1!=1:
	print("no")
