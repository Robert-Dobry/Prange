import service, isd_functions, time

n = [40,80,120,160,200]
t = [1,0]
n_test = 20
attempts_plain = 0
attempts_hints = 0
max_attempts = 5000

def calculate_max_error_cnt(n):
    k = int(n/2)
    gv = isd_functions.gilbert_varshamov_distance(n,k)
    return int((gv-1)/2)

# n_err = calculate_max_error_cnt(200)
# print(n_err)







