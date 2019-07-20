xaat1 = int(input())
taat = int(xaat1/2)
raat = []
for i in range(xaat1, taat, -1):
    j = str(i)
    if i + sum([int(kaat) for kaat in j]) == xaat1:
        print(1)
        print(i)
        break
else:
    print(0) 
