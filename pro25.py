xt=input()
lt1=list(map(int,input().split()))
max=0
i=0
while(i<len(lt1)-1):
    count=0
    while(i<len(lt1)-1 and lt1[i]<lt1[i+1]):
        count+=1
        i+=1
    if(count>max):
        max=count
    i+=1
print(max+1)
