from itertools import permutations
a =list(map(str,raw_input().split()))
a[1] = int(a[1])
b =list(permutations(a[0],a[1]))
b.sort()
for i in b:
    print(''.join(i))
