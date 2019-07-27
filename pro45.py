import sys, string, math

samt = input()
if samt == samt[::-1] :
    print('yes')
    sys.exit()
kimt = 0
for cust in samt[::-1] :
    if cust == '0' :
        kimt += 1
    else :
        break
sopt = '0'*kimt + samt

if sopt == sopt[::-1] :
    print('yes')
else :
    print('no')
