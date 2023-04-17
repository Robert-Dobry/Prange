import func as f
import math


t_length = 3

n = t_length * 8

k = int(n/2) if n%2==0 else int(n/2)+1

gv = f.gilbert_varshamov_distance(n,k)
print('GV:', gv)

t = [1,2,1]

if sum(t) > gv:
    raise TypeError("Sum of T cant be more than GV")
print(f"n: {n}")
print(f"k: {k}")


f.gen_inf_set_hints(t, n, k)


