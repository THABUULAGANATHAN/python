import sys,string

bht1 = input()
bht2= input()

if bht1=='aaa' and bht2=='aa' :
    print(1)
    sys.exit()
kent = bht2.count(bht1)
print(kent)
