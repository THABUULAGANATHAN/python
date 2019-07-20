nnt,mmt=map(int,input().split())
lt=[]
for _ in range(nnt):
	lt.append(sorted(list(map(int,input().split()))))
for i in range(nnt-1):
	for j in range(mmt):
		for k in range(nnt-i):
			if(lt[i][j]>lt[i+k][j]):
				lt[i][j],lt[i+k][j]=lt[i+k][j],lt[i][j]
for i in lt:
	print(*i,sep=' ')       
