import func as f
import math

n = 32
k = int(n/2) if n%2==0 else int(n/2)+1
w = 1

t = [5,3,2,1]

r = f.calculate_indexes(t,n, k)
print(r)

inf = f.gen_inf_set_hints(t,n,k)

