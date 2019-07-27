import sys,string, math, itertools

nt,kt = input().split()
nt,kt = int(nt),int(kt)
Leet = [ int(x) for x in input().split()]
#print(nt,kt, Leet)
for i in range(0,nt) :
    if (86400-Leet[i]) >= kt :
        print(i+1)
        sys.exit()
    kt -= (86400-Leet[i])
