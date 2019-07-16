bt=int(input())
xt=[]
for i in range(bt):
  at=input()
  xt.append(at)
mv2=min(xt,key=len)
xt.remove(mv2)
for i in range(len(mv2)):
  for j in range(len(xt)):
     cv2=xt[j]
     if mv2[:i+1]==cv2[:i+1]:
       result=mv2[:i+1]
     else:
       break
print(result)
