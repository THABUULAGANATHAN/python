nt=int(input())
liat=[]
at=nt//2+nt
for i in range(1,nt+1):
    if i%2==0:
        liat.append(i)
for i in range(1,nt+1):
    if i%2!=0:
        liat.append(i)
for i in range(1,nt+1):
    if i%2==0:
        liat.append(i)
print(at)
print(*liat)
