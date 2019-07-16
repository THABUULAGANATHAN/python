at=int(input())
rt=list(map(int,input().split()))
mt=0
for i in range(0,at):
  for j in range(0,i):
    if(rt[j]<rt[i]):
      mt=mt+rt[j]
print(mt)
