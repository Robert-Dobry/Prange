import func as f
import math

t = [1,2,3]

n = 8 * len(t)
k = int(n/2) if n%2==0 else int(n/2)+1
w = 1
print(n)
print(k)



indexes = f.calculate_indexes(t,n, k)
print(indexes)



