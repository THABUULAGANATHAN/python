nt=int(input())
bt=pow(2,nt)
at=[]
for i in range(bt):  
    ct=bin(i).replace("0bt","")
    at.append(ct.zfill(nt))
    at.sort(key=(lambda xt:xt.count('1')))
for i in at:
    print(i)
