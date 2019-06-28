t,k1=map(int,input().split())
for i in range(t+1,k1):
  sum=0
  num=i
  while(num>0):
    x=num%10
    num=num//10
    y=x**3
    sum=sum+y
  if(i==sum):
    print(sum,end=' ')
