import sys, string, math
def reduceNt( at, kt) :
	if kt <= 0 : return at

	if at == 0 : return 10	# Fail
	pt1 = reduceNt(at//10, kt)*10 + at%10
	pt2 = reduceNt(at//10, kt-1)
	if pt1 < pt2 :
		return pt1
	else :
		return pt2

at,kt = input().split()
at,kt = int(at),int(kt)
print(reduceNt(at,kt))

