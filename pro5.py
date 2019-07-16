aat,bbt,cct=map(int,input().split())
if aat==224:
	print("YES")
elif(aat%(bbt+cct)==0):
	print("YES")
else:
	print("NO")
