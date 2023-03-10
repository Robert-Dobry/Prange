from sage.all import *
from sage.coding import linear_code
import random, numpy

def generate_information_set(n,k):
    result = []
    for i in range(1,n+1):
        result.append(i)
    random.shuffle(result)
    result = result[:k]
    result.sort()
    return result
    

def generate_random_matrix(n,k):
    result = []
    for i in range(k):
        row_zeros = [0 for i in range(n)]
        row_zeros[i] = 1
        for j in range(k,n):
            row_zeros[j]=random.randint(0,1)
        result.append(row_zeros)
    
    return result


def get_minimum_distance(matrix):
    mat = Matrix(GF(2),matrix)
    C = linear_code.LinearCode(mat)
    return C.minimum_distance()


def print_matrix(matrix):
    for row in matrix:
        print('|', end=' ')
        for item in row:
            print(item, end=' ')
        print('|')


def print_set(set):
    print('|', end=' ')
    for item in set:
        print(item, end=' ')
    print('|')


def mask_vector(v, inf_set):
    result = []
    for number in inf_set:
        result.append(v[number])
    return result


def gen_random_codeword(G):
    f = GF(2)
    k = len(G)
    m = Matrix(f, [random.randint(0,1) for i in range(k)])
    g = Matrix(f, G)
    result = m*g 
    return result


def main():
    n = 4
    k = 2
    i = generate_information_set(n,k)
    print('\nInformation set:')
    print_set(i)
    
    g = generate_random_matrix(n,k)
    print('\nGenerator matrix:')
    print_matrix(g)
    
    print('\nRandom codeword(m*G, where m is random vector of gf(2)):')
    r = gen_random_codeword(g)
    print_matrix(r)
    

main()