import random, numpy, math


def mask_matrix(m, inf_set):
    result = []
    for row in m:
        result.append(mask_vector(row,inf_set))
    return result


def hwt(v):
    result = 0
    for item in v:
        if item>0:
            result+=1
    return result


def substract_vectors_numpy(a,b):
    return numpy.mod(numpy.subtract(a,b),2)


def substract_vectors(a,b):
    result = []
    for i in range(len(a)):
        result.append((a[i]-b[i])%2)
    return result




def inverse_matrix(m):
    det = int(numpy.linalg.det(m))
    if det == 0:
        return []
    else:
        result = numpy.mod(numpy.linalg.inv(m),2)
        return result


def matrix_multiply(x, A):
    x = numpy.array(x, dtype=numpy.int8)
    A = numpy.array(A, dtype=numpy.int8)
    result = [int(x) for x in numpy.mod(numpy.dot(x,A),2)]
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



def gen_random_e_with_hints(t,n):
    result = []
    for ti in t:
        subresult = []
        subresult += zeros(int(n/2))
        while hwt(subresult) < ti:
            subresult[random.randint(0,len(subresult)-1)] = 1
        result += subresult
    return result


def gen_random_message(n):
    result = []
    for i in range(n):
        result.append(random.randint(0,1))
    return result


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


def gen_inf_set_with_x(x, n, k): # x = [4,4]
    result = []
    N_sections = gen_2_sections(n)
    i = 0
    for xi in x:
        subresult = []
        while len(subresult) < xi:
            random_index = random.randint(0,int(n/2)-1)
            random_num = N_sections[i][random_index]
            if random_num not in subresult:
                subresult.append(random_num)
        subresult.sort()
        result += subresult
        i+=1
    return result


def gen_2_sections(n):
    result = []
    num = 1
    for i in range(2):
        ni = []
        for j in range(int(n/2)):
            ni.append(num)
            num+=1
        result.append(ni)
    return result
        
    
def calculate_cardinalities(t, n):
    result = []
    n_sections = len(t)
    if n % n_sections == 0:
        for i in range(n_sections):
            result.append( int( n/n_sections ) )
        return result
    else:
        raise TypeError("Length of t must divide n")


def calculate_indexes(t,n,k):
    cardinalities = calculate_cardinalities(t,n)
    x = [(cardinalities[i] - t[i]) for i in range(len(t))] # define initial X
    if sum(x) == k:
        return x
    length = len(x)
    overlap = sum(x) - k
    for i in range(overlap):
        max_prob = 0
        idx = None
        for j in range(length):
            x_copy = x.copy()
            x_copy[j]-=1
            if (x_copy[j] < 0):
                continue
            p = Pprange(x_copy, t, n)
            if p > max_prob:
                max_prob = p
                idx = j
        x[idx] -= 1
        x_copy = x.copy()
    return x


def Pprange(x, t, n): # calculates probabilty of success of ISD with given T decomposition
    result = 1
    lenght = len(x)
    ni = int(n/2)
    for i in range(lenght):
        result *= (math.comb(ni-x[i], t[i])) / math.comb(ni, t[i])
    return result


def PPlainISD(n,k,w):
    base = math.comb(n-k,w)
    divider = math.comb(n,w)
    result = base/divider
    return result


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


def gilbert_varshamov_distance(n,k):
    r = n-k
    d = 1
    bound = 2**r
    while True:
        summ = sumNcR(d-1, n) # sum from 0 to d including
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


    
