import service, func, time

n = 100
t = [1,0]
n_test = 0
attempts_plain = 0
attempts_hints = 0
max_attempts = 10000

# print(f'n : {n}')
# print(f't: {t}')
# print(f"running isd algorithm for {n_test} times..")
tic = time.perf_counter()
for i in range(n_test):
    data_gen_time1 = time.perf_counter()
    data = service.generate_data(t,n)
    data_gen_time2 = time.perf_counter()
    print(f'test number {i+1}')
    plain_output = service.decode_plain_isd(data, max_attempts)
    attempts_plain += plain_output["n_attempts"]
    print('attempt count: ', plain_output["n_attempts"])
    # hints_output = service.decode_with_hints(data, max_attempts)
    # attempts_hints += hints_output["n_attempts"]
    # print('attempt count: ', hints_output["n_attempts"])

# toc = time.perf_counter()
# data_gen_time_len = (data_gen_time2 - data_gen_time1) * n_test
# time_len = toc - tic - data_gen_time_len

# hints_prob = data["prob_hints"]
# plain_prob = data["prob_plain"]

# n_expected_plain = 1/plain_prob
# n_expected_hints = 1/hints_prob

# print(f'expected attempt count for Plain ISD: {int(n_expected_plain)}')
# print(f'expected attempt count for ISD w Hints: {int(n_expected_hints)}')

# avg_hints =  attempts_hints / n_test
# avg_plain = attempts_plain / n_test

# print(f'average attempts for decode plain ISD: {avg_plain}')
# print(f'average attempts for decode isd with hints: {avg_hints}')
# print(f'time elapsed: {time_len:0.4f} seconds')
# print(f'data generation time: {data_gen_time_len:0.4f} seconds')





p1 = func.PPlainISD(20,10,1)
p2= func.PPlainISD(80,40,1)

print(p1, p2)




