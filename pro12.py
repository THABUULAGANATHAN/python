mt,rt=list(map(int,input().split()))
lis1=list(map(int,input().split()))
for i in range(rt):
  ut1,vt1=list(map(int,input().split()))
  print(sum(lis1[ut1-1:vt1]))
