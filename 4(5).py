thab=input()
thabu=0
for i in range(len(thab)):
  if(thab[i].isdigit() or thab[i].isalpha() or thab[i]==(" ")):
    continue
  else:
    thabu+=1
print(thabu)
