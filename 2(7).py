num1=int(input())
t=num1
k=0
while(num1>0):
  var1=num1%10
  num1=num1//10
  var2=var1**3
  k=k+var2
if(t==k):
  print("yes")
else:
  print("no")

