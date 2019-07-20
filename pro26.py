def sub(rt): 
    mt = len(rt) 
    sub = [1]*mt 
    for i in range (1 , mt): 
        for j in range(0 , i): 
            if rt[i] > rt[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(mt): 
        maximum = max(maximum , sub[i])  
    return maximum
ar1=int(input()) 
rt = list(map(int,input().split()))
print (sub(rt))
