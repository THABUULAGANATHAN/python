k,t1=map(int,input().split())
for i in range(k + 1,t1):
  if i > 1:
    for y in range(2,i):
      if(i % y) == 0:
        break
    else:
      print(i,end=" ")
