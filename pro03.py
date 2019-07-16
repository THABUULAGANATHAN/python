import sys, string, math
st1,st2 = input().split()
nt1 = len(st1)
nt2 = len(st2)
if nt2 > nt1 :
    i = 0
    while i<nt1 and st1[i] == st2[i] :
        i += 1
    print(nt2-i)
elif nt2 == nt1 :
    i = 0
    while i<nt2 and st1[i] == st2[i] :
        i += 1
    print(nt2-i)
else :

    i = 0
    while i<nt2 and st1[i] == st2[i] :
        i += 1
    st31 = st1[i:]
    st32 = st2[i:]
    Lt = list(st31)
    kt = 0
    for ct in st32 :
        if ct in Lt :
            kt += 1
            Lt.remove(ct)
    print(nt1-i-kt)
