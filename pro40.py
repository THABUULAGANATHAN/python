stt1="dhoni"
stt2=input()
valt1=list(set(stt1)-set(stt2))
valt2=list(set(stt2)-set(stt1))
valt=len(valt1)+len(valt2)
if valt==0:
	print("yes")
else:
	print("no")
