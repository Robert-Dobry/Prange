import service, isd_functions, time, random


def calculate_max_error_cnt(n):
    k = int(n/2)
    gv = isd_functions.gilbert_varshamov_distance(n,k)
    return int((gv-1)/2)


def test_plain_isd(n_list, n_test, max_attempts):
    for n in n_list:
        k = int(n/2)
        w = calculate_max_error_cnt(n)
        t = create_t_by_max_error_cnt(w)
        P = isd_functions.PPlainISD(n,k,w)
        attempts = 0
        tic = time.perf_counter()
        print(f'\nTest for Plain ISD: n={n}, w={w} {n_test} times.')
        for i in range(n_test):
            print('test: ',i+1)
            data = service.generate_data(t,n)
            output = service.decode_plain_isd(data, max_attempts)
            attempts += output["n_attempts"]
        tac = time.perf_counter()
        avg_attempts = attempts/n_test
        avg_duration = (tac - tic)/n_test
        print(f'Succes probability (1 iteration): {P}')
        print(f'Average attempt count: {avg_attempts}')
        print(f'Average duration: {avg_duration:0.3f}')


def create_t_by_max_error_cnt(err_cnt):
    t = [0,0]
    while sum(t) < err_cnt:
        t[random.randint(0,1)] += 1
    return t


n_all = [200,]
n_test = 5
max_attempts = 5000
test_plain_isd(n_all, n_test, max_attempts)






