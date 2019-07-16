kt1,l1=map(str,input().split())
yast=0
if len(kt1)>len(l1):
  kt1,l1=l1,kt1
pt1=0
while pt1<len(kt1):
  yast+=(ord(l1[pt1])-ord(kt1[pt1]))
  pt1+=1
for pt1 in range(pt1,len(l1)):
  yast+=ord(l1[pt1])-ord('a')+1
print(yast)
