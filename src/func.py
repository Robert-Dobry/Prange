import random, numpy, math

def mask_matrix(m, inf_set):
    result = []
    for row in m:
        result.append(mask_vector(row,inf_set))
    return result


def vector_str(v):
    str_v = [str(n) for n in v]
    result = " "
    result = '<p>' + result.join(str_v)+ '</p>'
    return result


def matrix_str(m):
    result = ""
    for row in m:
        result+=vector_str(row)
    return result


def hwt(v):
    result = 0
    for item in v:
        if item>0:
            result+=1
    return result


def inverse_matrix(m):
    det = int(numpy.linalg.det(m))
    if det == 0:
        return []
    else:
        result = numpy.mod(numpy.linalg.inv(m),2)
        return result


def mat_mul(a,b):
    x = numpy.dot(a,b)
    result = []
    for item in x:
        result.append(item%2)
    return result


def multiply_gf2(x, A):
    x = numpy.array(x, dtype=numpy.int8)
    A = numpy.array(A, dtype=numpy.int8)
    return numpy.mod(numpy.dot(x,A),2)


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
    index = random.randint(0,len(g)-1)
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


def check_input():
    pass


def calculate_cardinalities(t, n):
    result = []
    n_sections = len(t)
    if n % n_sections == 0:
        for i in range(n_sections):
            result.append( int( n/n_sections ) )
        return result
    else:
        raise TypeError("Length of t must divide n")

    # x = []
    # while(sum(x) < n):
    #     x.append(math.ceil(n/n_sections))
    # while(sum(x) > n):
    #     x[-1] -= 1
    #     if x[-1] < t[-1]:
    #         return -1
    # return x


def calculate_indexes(t,n):
    
    

    cardinalities = []




def remainder_division(a,b):
    count = 0
    incr = a
    remainder = a-b
    while(a <= b):
        count+=1
        a+=incr
    remainder = b - (a - incr) 
    return count,remainder
     

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


def gilbert_varshamov_distance(A):
    k, n = numpy.shape(A)
    r = n-k
    d = 1
    bound = 2**r
    while True:
        summ = sumNcR(d-1, n) # sum from 0 to d including
        print('suma: ', summ, 'd: ', d)
        cond = (summ <= 2**r)
        if (cond):
            d+=1
        else:
            return d-1


def print_matrix(m):
    for row in m:
        print('|',end=' ')
        for num in row:
            print(num, end=' ')
        print('|')


def float_to_int(a):
    result = []
    for row in a:
        new_row = []
        for item in row:
            new_row.append(int(item))
        result.append(new_row)
    return result


def print_set(r):
    print('|', end=' ')
    for num in r:
        print(num, end=' ')
    print('|')
        

def sumNcR(d,n):
    summary = 0
    if d == 0:
        return summary
    for i in range(d+1):
        addition = math.comb(n,i)
        summary += addition
    return summary



