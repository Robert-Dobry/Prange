import func as f

DATA = None
HINTS = []

def generate_data(t,n):

    if ' ' in t:
        t = t.split()
        t = [int(item) for item in t]
    else:
        t = [int(char) for char in t]
  
    result = {}
    k = int(n/2) if n%2==0 else int(n/2)+1 
    g_matrix = f.generate_matrix(n,k) # ISD INPUT
    gv_distance = f.gilbert_varshamov_distance(n,k)
    max_n_errors = int((gv_distance-1)/2)
    message = f.gen_random_message(k)
    error_vector = f.gen_random_e_with_hints(t, n)
    omega = sum(t)
    received_vector = f.multiply_gf2(message, g_matrix)
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
    

def create_code(t_len):
    n = int(t_len) * 8
    k = int(n/2) if n%2==0 else int(n/2)+1 
    matrix = f.generate_matrix(n,k)
    return matrix

def gilbert_varshamov_dist(n):
    k = int(n/2)
    gv = f.gilbert_varshamov_distance(n,k)
    return gv


def decode_plain_isd(data, attempts):
    n = data["n"]
    k = data["k"]
    n_attemps = 0
    prob = f.PPlainISD(n,k, data["omega"])
    while True and n_attemps < attempts:
        n_attemps += 1
        inf_set = f.gen_information_set(n,k)
        masked_matrix = f.mask_matrix(data["gen_matrix"], inf_set)
        masked_vector = f.mask_vector(data["received_vector"], inf_set)
        inverse_masked_matrix = f.inverse_matrix(masked_matrix)
        if inverse_masked_matrix==[]:
            continue
        x_vector = f.multiply_gf2(masked_vector, inverse_masked_matrix)
        xG = f.multiply_gf2(x_vector, data["gen_matrix"])
        xG_plus_r = f.add_vectors(xG, data["received_vector"])
        error = f.multiply_gf2(masked_vector, inverse_masked_matrix)
        error = f.multiply_gf2(error, data["gen_matrix"])
        error = f.substract_vectors(data["received_vector"], error)
        hamming_w = f.hwt(xG_plus_r)
        if hamming_w <= data["omega"]:
            return {"decode_type" : "Plain ISD",
                    "vector" : x_vector,
                    "error" : error,
                    "n_attempts": n_attemps}
        else:
            continue
    return {
        "decode_type" : "Plain ISD",
        "n_attempts" : n_attemps
    }


def decode_with_hints(data, attempts):
    n = data["n"]
    k = data["k"]
    t = data["t_hints"]
    n_attemps = 0
    inf_set_indexes = f.calculate_indexes(t,n,k)
    prob = f.Pprange(inf_set_indexes, t,n)
    print(prob)
    while True and n_attemps < attempts:
        n_attemps += 1
        print("attempt: ", n_attemps)
        inf_set = f.gen_inf_set_with_x(inf_set_indexes, n,k)
        masked_matrix = f.mask_matrix(data["gen_matrix"], inf_set)
        masked_vector = f.mask_vector(data["received_vector"], inf_set)
        inverse_masked_matrix = f.inverse_matrix(masked_matrix)
        if inverse_masked_matrix==[]:
            continue
        x_vector = f.multiply_gf2(masked_vector, inverse_masked_matrix)
        xG = f.multiply_gf2(x_vector, data["gen_matrix"])
        xG_plus_r = f.add_vectors(xG, data["received_vector"])
        error = f.multiply_gf2(masked_vector, inverse_masked_matrix)
        error = f.multiply_gf2(error, data["gen_matrix"])
        error = f.substract_vectors(data["received_vector"], error)
        hamming_w = f.hwt(xG_plus_r)
        if hamming_w <= data["omega"]:
            return {"decode_type" : "ISD with Hints",
                    "vector" : x_vector,
                    "error" : error,
                    "n_attempts": n_attemps}
        else:
            continue
    return {
        "decode_type" : "ISD with Hints",
        "n_attempts" : n_attemps
    }