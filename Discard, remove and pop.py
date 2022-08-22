n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c = input().split()
    if c[0] == "pop":
        s.pop()
    elif c[0] == "remove":
        if int(c[1]) in s:
            s.remove(int(c[1]))
    elif c[0] == "discard":
        s.discard(int(c[1]))
sum = 0
for i in s:
    sum += i
print(sum)
