mynum1=int(input())
ans=0
while mynum1 > 0:
    ma= mynum1 % 10
    ans = ans + ma
    mynum1 = int(mynum1/10)
print(ans)
