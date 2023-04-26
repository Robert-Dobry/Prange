import func as f
import math, random


def main(t_len):
    result = {}
    n = int(t_len) * 8
    k = int(n/2) if n%2==0 else int(n/2)+1 

    matrix = f.generate_matrix(n,k)
    result["matrix"] = matrix

    gv = f.gilbert_varshamov_distance(n,k)
    result["gv"] = gv

    return result
    

def create_code(t_len):
    n = int(t_len) * 8
    k = int(n/2) if n%2==0 else int(n/2)+1 
    matrix = f.generate_matrix(n,k)
    return matrix

def gilbert_varshamov_dist(t_len,k):
    n = t_len * 8
    gv = f.gilbert_varshamov_distance(n,k)
    return gv

# t_length = 4
# n = t_length * 8
# k = int(n/2) if n%2==0 else int(n/2)+1
# gv = f.gilbert_varshamov_distance(n,k)
# print('GV: ', gv)
# t = f.zeros(t_length)
# n_errors = int(math.floor(gv-1)/2)

