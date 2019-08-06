bht=input()
surt=[]
for i in bht:
  if i not in surt:
    surt.append(i)
  else:
    break  
print(len(surt))
