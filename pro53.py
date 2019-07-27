import sys, string, math
sist = input()
sist = sist.lower()
sont = string.ascii_lowercase

for c in sont :
    if c not in sist :
        print('no')
        sys.exit()
print('yes')
