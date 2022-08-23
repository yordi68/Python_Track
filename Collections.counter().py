from collections import Counter
n = int(raw_input())
stock=list(map(int,raw_input().split(' ')))
dict=Counter(stock)
p=0
k=int(raw_input())
for i in range(k):
    size,price=map(int,raw_input().split())
    if dict[size]:
        dict[size]-=1
        p+=price        
print(p) 
