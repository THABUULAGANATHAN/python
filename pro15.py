ct=int(input())
dt=list(map(int,input().split(" ")))
dt=[bin(i) for i in dt]
dt.sort(reverse=True)
dt=[int(ct,2) for ct in dt]
for i in range(0,ct):
     print(dt[i])
