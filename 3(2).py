k1=int(input())
arr=list(map(int,input().split()[:k1]))
rra=sorted(arr,reverse=True)
print(rra[0])
