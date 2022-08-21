from itertools import product
a = raw_input()
b = raw_input()
a_list = a.split()
b_list = b.split()
list_a = list(map(int,a_list))
list_b = list(map(int,b_list))
a = list(product(list_a,list_b))
print(' '.join(str(x) for x in a))
