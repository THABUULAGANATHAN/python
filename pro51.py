def charm(l):
        bht=1
        
        for xt in range(0,len(l)-1):
                if l[xt]!=l[xt+1]:
                        bht=bht+1
                else:
                    break
        return bht
num1=int(input())
hiit=list(map(int,input().split()))

for xt in range(0,len(hiit)):
        if hiit[xt]>0:
                hiit[xt]=1
        else:
             hiit[xt]=0
A1=""

for xt in range(0,len(hiit)):
        B1=hiit[xt::]
        A1=A1+str(charm(B1))+" "
print(A1.strip())
