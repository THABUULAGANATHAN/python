at1=int(input())
bt1=pow(2,at1)
zt1=[]
for i in range(bt1):  
    mt1=bin(i).replace("0b","")
    zt1.append(mt1.zfill(at1))
    zt1.sort(key=(lambda x:x.count('1')))
for i in zt1:
    print(i)
