import func as f
import math, random


t_length = 10


n = t_length * 8

k = int(n/2) if n%2==0 else int(n/2)+1

gv = f.gilbert_varshamov_distance(n,k)
print('GV: ', gv)

t = f.zeros(t_length)
n_errors = int(math.floor(gv-1)/2)
print("allowed error count:", n_errors)
for i in range(n_errors):
    t[random.randint(0,t_length-1)]+=1

print("t: ",t)    
if sum(t) > math.floor((gv-1)/2):
    raise TypeError("Sum of T cant be more than (GV-1)/2")
print(f"n: {n}")
print(f"k: {k}")


i= f.gen_inf_set_with_hints(t, n, k)
print(i)



