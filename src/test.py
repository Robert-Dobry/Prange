import service, func

n = 20
t = [1,1]
n_test = 20
attempts_plain = 0
attempts_hints = 0
max_attempts = 10000

print(f'n : {n}')
print(f't: {t}')
data = service.generate_data(t,n)
print(f"running isd algorithm for {n_test} times..")
for i in range(n_test):
    
    plain_output = service.decode_plain_isd(data, max_attempts)
    attempts_plain += plain_output["n_attempts"]
    hints_output = service.decode_with_hints(data, max_attempts)
    attempts_hints += hints_output["n_attempts"]


hints_prob = data["prob_hints"]
plain_prob = data["prob_plain"]

n_expected_plain = 1/plain_prob
n_expected_hints = 1/hints_prob

print(f'expected attempt count for Plain ISD: {int(n_expected_plain)}')
print(f'expected attempt count for ISD w Hints: {int(n_expected_hints)}')

avg_hints =  attempts_hints / n_test
avg_plain = attempts_plain / n_test

print(f'average attempts for decode plain ISD: {avg_plain}')
print(f'average attempts for decode isd with hints: {avg_hints}')









