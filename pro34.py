xt,yt=map(int,input().split())
mnt1=0
Li1=[]
for i in range(xt):
      Li1.append(input())
for i in range(xt):
      for j in range(yt-1):
            if(Li1[i][j]!='R' and Li1[i][j+1]!='R'):
                  mnt1+=3
            elif(Li1[i][j]!='G' and Li1[i][j+1]!='G'):
                  mnt1+=5
print(mnt1)
