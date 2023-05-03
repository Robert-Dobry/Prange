import func as f
import math, random, json, numpy

DATA = None

def generate_data(t_len):
    result = {}
    n = int(t_len) * 8
    k = int(n/2) if n%2==0 else int(n/2)+1 

    g_matrix = f.generate_matrix(n,k) # ISD INPUT
    gv_distance = f.gilbert_varshamov_distance(n,k)

    max_n_errors = int((gv_distance-1)/2)
    print(max_n_errors)
    message = f.gen_random_message(k)
    omega = random.randint(0,max_n_errors) # ISD INPUT

    t_hints = f.gen_random_t(t_len, omega) # ISD INPUT
    error_vector = f.gen_random_e_with_hints(t_hints)

    received_vector = f.multiply_gf2(message, g_matrix)
    received_vector = f.add_vectors(received_vector, error_vector)

    result["n"] = n
    result["k"] = k
    result["gen_matrix"] = g_matrix
    result["gv_distance"] = gv_distance
    result["max_n_errors"] = max_n_errors

    result["message_vector"] = message
    result["omega"] = omega
    result["t_hints"] = t_hints
    result["error_vector"] = error_vector

    result["received_vector"] = received_vector
    return result
    

def create_code(t_len):
    n = int(t_len) * 8
    k = int(n/2) if n%2==0 else int(n/2)+1 
    matrix = f.generate_matrix(n,k)
    return matrix

def gilbert_varshamov_dist(t_len,k):
    n = t_len * 8
    gv = f.gilbert_varshamov_distance(n,k)
    return gv


def decode_plain_isd(data):
    n = data["n"]
    k = data["k"]
    n_attemps = 0
    while True and n_attemps < 5000:
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
        "n_attempts" : n_attemps
    }



