n,t2=map(int,input().split())
if(t2<=100000):
    for x in range(n+1,t2):
        if(x%2!=0):
          print(x,end=" ")
