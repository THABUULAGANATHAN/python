get=int(input())
set=list(map(int,input().split()))
go=0
for one1 in range(get):
    for two2 in range(one1,get):  
        for three3 in range(two2,get):
            if set[one1]<set[two2]<set[three3]:
                go+=1
print(go)
