st=int(input())
mt=0
for vt in range(0,st):
  if(pow(2,vt)>st):
    break
  mt=st-pow(2,vt)
print(mt)
