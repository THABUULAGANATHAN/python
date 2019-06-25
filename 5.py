import sys
u,v,w=map(int,(input().split()))
if u>v and u>w:
  print(u)
elif v>w:
  print(v)
else:
  print(w)
