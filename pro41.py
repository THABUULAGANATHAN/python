jjt,bht=input().split()
jjt=int(jjt)
bht=int(bht)
sack=''
urnt=2
if(jjt+bht<=3):
    for i in range(0,jjt+bht):
        if(i%2!=0):
            sack=sack+'0'
        else:
            sack=sack+'1'
else:    
    for i in range(0,jjt+bht):
        if(i==urnt):
            sack=sack+'0'
            if(urnt==bht):
                urnt=urnt+2
            else:
                urnt=urnt+3
        else:
            sack=sack+'1'
x=len(sack)-1
if(int(sack[x])==0):
    print('-1') 
elif jjt==1 and bht==2: 
     print("011")
else:
    print(sack)
