mt=int(input())
ct=0
lt=[]
for i in range(1,mt+1):
  lt.append(i)
for i in range(len(lt)):
  for i in range(i+1,len(lt)):
    ct+=1
print(ct)
