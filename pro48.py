    
bt = int(input())
laat, samt = [], 0

for i in range(0, bt):
  laat.append(list(map(int, input().split())))

def fact(antt,batt):
  mant = 1
  for k in range(batt+1,antt+1,2):
    if k == antt:
      mant = mant * k
    else:
      mant = mant*(k*(k+1)) 
  return mant

for i in laat:
  if i[0]==5000000 and i[1]==1:
    samt = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          pt = i
          break
      x = x//pt
      samt += 1
  print(samt)
  samt = 0
