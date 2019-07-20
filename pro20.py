nnnt,mmmt=list(map(int,input().split()))
lt=list(map(int,input().split()))
lt.sort(reverse=True)
ct=0
for i in lt:
    if mmmt==0:
        break
    qt=mmmt // i
    ct+=qt
    mmmt=mmmt-i*qt
print(ct)
