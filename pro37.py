
nt=int(input())
lt=list(map(int,input().split()))
ct=0
it=0
while(it<len(lt)):
    tt=lt[it]
    if(it==0):
        if(len(lt)==1):
            ct=1 
            break
    elif(i==len(lt)-1):
        ct=ct
    else:
        if(tt>l[it+1] and tt>l[it-1]):
            ct=ct+1
        elif(tt<l[it-1] and tt<l[it+1]):
            ct=ct+1
    it=it+1
print(ct)
