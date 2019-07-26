import sys,string


def maxOfSegmentMins(Lact, nect, kint):
    if kint == 1:
        return min(Lact)
    if kint == 2 :
        return max(Lact[0], Lact[nect - 1])
    return max(Lact)

nect,kint = input().split()
nect,kint = int(nect),int(kint)
Lact = [ int(x) for x in input().split()]
nect = len(Lact)
ans = maxOfSegmentMins(Lact, nect, kint)
print(ans)
