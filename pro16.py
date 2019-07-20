ntn1=int(input())
li1=list(map(int,input().split()))
at=[1]*ntn1
for dt in range(ntn1):
    if(dt==0):
        if(li1[dt]>li1[dt+1]):
            at[dt]=at[dt]+at[dt+1]
    elif(dt>0):
        if(li1[dt]>li1[dt-1]):
            at[dt]=at[dt]+at[dt-1]
print(sum(at))
