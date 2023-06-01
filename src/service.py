import isdfunctions as f

DATA = None
HINTS = []


def parse_t(t_string, n):

    t = []
    for item in t_string:
        if item != ' ' and not item.isnumeric():
            return "<b> t must be numeric value!</b>"

    if ' ' in t_string:
        t = t_string.split()
        if len(t) != 2:
            return "<b> t must be of length 2!</b>"
        t = [int(item) for item in t]
    else:
        if len(t_string) != 2:
            return "<b> t must be of length 2!</b>"
        t = [int(item) for item in t_string]
    if sum(t) > int(n):
        return "<b> sum of t cannot be more than n </b>"
    return t
        
def generate_data(t,n):
  
    result = {}
    k = int(n/2) if n%2==0 else int(n/2)+1 
    g_matrix = f.generate_matrix(n,k) # ISD INPUT
    gv_distance = f.gilbert_varshamov_distance(n,k)
    max_n_errors = int((gv_distance-1)/2)
    message = f.gen_random_message(k)
    error_vector = f.gen_random_e_with_hints(t, n)
    omega = sum(t)
    received_vector = f.matrix_multiply(message, g_matrix)
    received_vector = f.add_vectors(received_vector, error_vector)
    indexes_for_inf_set = f.calculate_indexes(t,n,k)
    prob_hints = round(f.Pprange(indexes_for_inf_set, t,n), 8)
    prob_plain = round(f.PPlainISD(n,k,omega),8)
    user_message = []
    if 0 in t:
        user_message.append("Please note, that with this error decomposition, information set for ISD with hints will be the same over every iteration, therefore ISD with hints may not work in this case.")
    if omega > max_n_errors:
        user_message.append("Please note, that error count is bigger than maximum amount of errors this code can fix, therefore output may not be correct")

    result["n"] = n
    result["k"] = k
    result["gen_matrix"] = g_matrix
    result["gv_distance"] = gv_distance
    result["max_n_errors"] = max_n_errors
    result["prob_hints"] = prob_hints
    result["prob_plain"] = prob_plain
    result["message_vector"] = message
    result["omega"] = omega
    result["t_hints"] = t
    result["error_vector"] = error_vector
    result["vector_x"] = indexes_for_inf_set
    result["received_vector"] = received_vector
    result["message_for_user"] = user_message
    return result
    

def gilbert_varshamov_dist(n):
    k = int(n/2)
    gv = f.gilbert_varshamov_distance(n,k)
    return gv


def decode_plain_isd(data, attempts):
    n = data["n"]
    k = data["k"]
    n_attemps = 1
    n_not_inv = 0
    while True and n_attemps < attempts:
        inf_set = f.gen_information_set(n,k)
        masked_matrix = f.mask_matrix(data["gen_matrix"], inf_set)
        masked_vector = f.mask_vector(data["received_vector"], inf_set)
        inverse_masked_matrix = f.inverse_matrix(masked_matrix)
        if inverse_masked_matrix==[]:
            n_not_inv += 1
            #print("not inv: ", n_not_inv)
            continue
        x_vector = f.matrix_multiply(masked_vector, inverse_masked_matrix)
        xG = f.matrix_multiply(x_vector, data["gen_matrix"])
        xG_plus_r = f.add_vectors(xG, data["received_vector"])
        hamming_w = f.hwt(xG_plus_r)
        if hamming_w <= data["omega"]:
            return {"decode_type" : "Plain ISD",
                    "vector" : x_vector,
                    "error" : xG_plus_r,
                    "n_attempts": n_attemps,
                    "n_inv" : n_not_inv}
        else:
            n_attemps += 1
            #print("attempt: ", n_attemps)
            continue
    return {
        "decode_type" : "Plain ISD",
        "n_attempts" : n_attemps
    }


def decode_with_hints(data, attempts):
    n = data["n"]
    k = data["k"]
    t = data["t_hints"]
    n_not_inv = 0
    n_attemps = 1
    inf_set_indexes = f.calculate_indexes(t,n,k)
    while True and n_attemps < attempts:
        inf_set = f.gen_inf_set_with_x(inf_set_indexes, n,k)
        masked_matrix = f.mask_matrix(data["gen_matrix"], inf_set)
        masked_vector = f.mask_vector(data["received_vector"], inf_set)
        inverse_masked_matrix = f.inverse_matrix(masked_matrix)
        if inverse_masked_matrix==[]:
            n_not_inv += 1
            #print("not inv: ", n_not_inv)
            continue
        x_vector = f.matrix_multiply(masked_vector, inverse_masked_matrix)
        xG = f.matrix_multiply(x_vector, data["gen_matrix"])
        xG_plus_r = f.add_vectors(xG, data["received_vector"])
        hamming_w = f.hwt(xG_plus_r)
        if hamming_w <= data["omega"]:
            return {"decode_type" : "ISD with Hints",
                    "vector" : x_vector,
                    "error" : xG_plus_r,
                    "n_attempts": n_attemps,
                    "n_inv" : n_not_inv}
        else:
            n_attemps += 1
            #print("attempt: ", n_attemps)
            continue
    return {
        "decode_type" : "ISD with Hints",
        "n_attempts" : n_attemps
    }