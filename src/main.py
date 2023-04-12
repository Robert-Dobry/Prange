import func as f
import math

n = 28
k = int(n/2) if n%2==0 else int(n/2)+1
w = 1

t = [5,3,2,7]

r = f.calculate_cardinalities(t,n)

print(r)

#f.calculate_indexes(t, n)

