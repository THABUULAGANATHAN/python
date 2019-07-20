size8=int(input())
arr3=[]
for i in range(size8):
	st=input()
	st=list(map(int,st.split(" ")))
	lt=len(st)
	for j in range(lt):
		arr3.append(st[j])
arr3.sort()
print(*arr3,sep=" ")	
