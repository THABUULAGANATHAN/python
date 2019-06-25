import sys
yr=int(input())
if yr%400==0 or (yr%4==0 and yr%100!=0):
  print("yes")
else:
  print("no")
