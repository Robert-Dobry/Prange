import random, numpy

def mask_matrix(m, inf_set):
    result = []
    for row in m:
        result.append(mask_vector(row,inf_set))
    return result


def mat_mul(a,b):
    result = numpy.dot(a,b)
    return result


def add_vectors(a,b):
    result = []
    if len(a) != len(b):
        return -1
    else:
        size = len(a)
        for i in range(size):
            result.append((a[i]+b[i]) % 2)
    return result


def gen_random_e(n,w):
    result = [0 for i in range(n)]
    indexes = gen_information_set(n,w)
    for i in indexes:
        result[i-1] = 1
    return result
    

def gen_random_codeword(g):
    #m = [random.randint(0,1) for i in range(n)]
    index = random.randint(0,k-1)
    return g[index]


def mask_vector(v, inf_set):
    result = []
    for index in inf_set:
        result.append(v[index-1])
    return result
        

def gen_information_set(n,k):
    result = [i+1 for i in range(n)]
    random.shuffle(result)
    result=result[:k]
    result.sort()
    return result


def zeros(n):
    return [0 for i in range(n)]


def generate_matrix(n,k):
    result = []
    for i in range(k):
        result.append(zeros(n))
    for i in range(k):
        result[i][i] = 1
    for i in range(k):    
        for j in range(k,n):
            result[i][j] = random.randint(0,1)
    return result


def print_matrix(m):
    for row in m:
        print('|',end=' ')
        for num in row:
            print(num, end=' ')
        print('|')


def print_set(r):
    print('|', end=' ')
    for num in r:
        print(num, end=' ')
    print('|')
        

n=4
k=2
w = 1

inf_set=gen_information_set(n,k)
m = generate_matrix(n,k)
r = gen_random_codeword(m)
e = gen_random_e(n,w)
p = add_vectors(r,e)
masked_m=mask_matrix(m,inf_set)
masked_r=mask_vector(p,inf_set)
x = mat_mul(masked_r, masked_m)


print('\ninf set:')
print_set(inf_set)
print('\ngen matrix:')
print_matrix(m)
print('\nr:')
print_set(r)
print('\ne:')
print_set(e)
print('\ne+r:')
print_set(p)
print('\nmasked g:')
print_matrix(masked_m)
print('\nmasked r:')
print_set(masked_r)
print('\nx:')
print_set(x)
