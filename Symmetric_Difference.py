M = int(raw_input())
a = raw_input()
N = int(raw_input())
b = raw_input()
lis = a.split()
lis2 = b.split()
newlis = list(map(int, lis))
newlis2 = list(map(int, lis2))
myset1 = set(newlis)
myset2 = set(newlis2)
q = list((myset1.difference(myset2)).union(myset2.difference(myset1)))
q.sort()
for i in q:
    print i
