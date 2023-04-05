import func as f
import math

n = 6
k = int(n/2) if n%2==0 else int(n/2)+1
w = 1


matrix = f.generate_matrix(n,k)
d = f.gilbert_varshamov_distance(matrix)
print(d)

