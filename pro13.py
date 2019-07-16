mt,rt = input().split()
mt,rt = int(mt), int(rt)
Lt1 = [ int(x) for x in input().split()]
for i in range(0,rt) :
    at1,bt1 = input().split()
    at1,bt1 = int(at1), int(bt1)
for i in range(0,rt):
    print(min(Lt1[at1-1:bt1]))
