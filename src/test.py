import service, isdfunctions, time, random


def calculate_max_error_cnt(n):
    k = int(n/2)
    gv = isdfunctions.gilbert_varshamov_distance(n,k)
    return int((gv-1)/2)


def test_plain_isd(n, t, n_test, max_attempts):
    
    k = int(n/2)
    w = sum(t)
    P = isdfunctions.PPlainISD(n,k,w)
    attempts = 0
    tic = time.perf_counter()
    print(f'\nTest for Plain ISD: n={n}, w={w} {n_test} times.')
    for i in range(n_test):
        print('test: ', i+1)
        data = service.generate_data(t,n)
        output = service.decode_plain_isd(data, max_attempts)
        attempts += output["n_attempts"]
    tac = time.perf_counter()
    avg_attempts = attempts/n_test
    avg_duration = (tac - tic)/n_test
    print(f'Succes probability (1 iteration): {P}')
    print(f'Average attempt count: {avg_attempts}')
    print(f'Average duration: {avg_duration:0.3f}')
    print(f'Expected avg attempt count: {1/P}')


def test_hints_isd(n, t, n_test, max_attempts):
    
    k = int(n/2)
    x = isdfunctions.calculate_indexes(t,n,k)
    P = isdfunctions.Pprange(x,t,n)
    attempts = 0
    tic = time.perf_counter()
    print(x)
    print(f'\nTest for Plain ISD w Hints: n={n}, t={t} {n_test} times.')
    for i in range(n_test):
        print('test: ', i+1)
        data = service.generate_data(t,n)
        output = service.decode_with_hints(data, max_attempts)
        attempts += output["n_attempts"]
    tac = time.perf_counter()
    avg_attempts = attempts/n_test
    avg_duration = (tac - tic)/n_test
    print(f'Succes probability (1 iteration): {P}')
    print(f'Average attempt count: {avg_attempts}')
    print(f'Average duration: {avg_duration:0.3f}')
    print(f'Expected avg attempt count: {1/P}')


def create_t_by_max_error_cnt(err_cnt):
    t = [0,0]
    while sum(t) < err_cnt:
        t[random.randint(0,1)] += 1
    return t


# print(isd_functions.gilbert_varshamov_distance(200, 100))
# print(calculate_max_error_cnt(200))

# t = [4,7]
# n = 200
# n_test = 50
# max_att = 5000
# test_hihts_isd(n, t, n_test, max_att)









