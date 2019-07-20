k1=input()
for v in range(len(k1)):
  if(k1[v] < k1[v+1]):
    print(k1[v+1:])
    break
