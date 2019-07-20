ktr1=input()
for vt in range(len(ktr1)):
  if(ktr1[vt] < ktr1[vt+1]):
    print(ktr1[vt+1:])
    break
