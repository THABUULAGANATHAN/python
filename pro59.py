bht,sbt=map(str,input().split("|"))
cct=input()
if  len(bht)>len(sbt):
    if len(bht)==len(sbt)+len(cct):
        print(bht+"|"+sbt+cct)
elif len(bht)<len(sbt):
     if len(sbt)==len(bht)+len(cct):
        print(bht+cct+"|"+sbt)
elif len(bht)==len(sbt) and len(cct)>1 or (len(sbt) or len(bht)):
    print("impossible")
