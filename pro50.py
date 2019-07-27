xt,yt=map(int,input().split())
zt=[]

for i in range(yt):
  zt.append(list(map(int,input().split())))
maht=10000000
bht=0

for i in range(yt):
  if zt[i][0]==1:
    sont=zt[i][1]
    pict=zt[i][2]
    for j in range(i+1,yt):
      if zt[j][0]==sont:
        sont=zt[j][1]
        pict=pict+zt[j][2]
    if pict<maht and sont==xt:
      maht=pict
      bht=bht+1

if bht==0:
  print(-1)
else:
  print(maht)
