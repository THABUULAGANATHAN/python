import sys, string, math


def isPrime(num1) :
    if num1 <= 1 : return False
    if num1==2 or num1==3 : return True
    antt = int(math.sqrt(num1)+1)
    for i in range(2,antt+1) :
        if num1%i == 0 :
            return False
    return True

def factors1(num1) :
    Laat = []
    i = 2
    while num1 >1 :
        while num1%i == 0 :
            Laat.append(i)
            num1//= i
        i += 1
    return Laat
num1,kimt = input().split()
num1,kimt = int(num1), int(kimt)
if kimt==0 :
    print(num1)
    sys.exit()
antt = 10**kimt
if isPrime(num1) :
    print(num1 * antt)
    sys.exit()
sunt = str(num1)[::-1]
cnt0 = 0
for cct in sunt :
    if cct=='0' :
        cnt0 += 1
    else :
        break
if cnt0 >= kimt :
    print(num1)
    sys.exit()
Laat = factors1(num1)

cnt2 = Laat.count(2)
cnt5 = Laat.count(5)
if cnt2 + cnt5 == 0 :
    print(num1 * an1t)
    sys.exit()

if cnt2 < kimt and cnt5 < kimt :
    while 2 in Laat : Laat.remove(2)
    while 5 in Laat : Laat.remove(5)
elif cnt2 < cnt5 :
    while 2 in Laat :
        Laat.remove(2)
    if cnt5 > kimt :
        for i in range(kimt) :
            Laat.remove(5)
elif cnt5 < cnt2 :
    while 5 in Laat :
        Laat.remove(5)
    if cnt2 > kimt :
        for i in range(kimt) :
            Laat.remove(2)
pent = 1
for x in Laat :
    pent = pent * x
ant = pent * 10**kimt
print(ant)
