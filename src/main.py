import func as f
import math, random, json


def main(t_len):
    result = {}
    n = int(t_len) * 8
    k = int(n/2) if n%2==0 else int(n/2)+1 

    g_matrix = f.generate_matrix(n,k) # ISD INPUT
    gv_distance = f.gilbert_varshamov_distance(n,k)

    message = f.gen_random_message(k)
    omega = random.randint(1,gv_distance) # ISD INPUT

    t_hints = f.gen_random_t(t_len, omega)
    error_vector = f.gen_random_e_with_hints(t_hints)

    received_vector = f.multiply_gf2(message, g_matrix)
    received_vector = f.add_vectors(received_vector, error_vector)

    result["gen_matrix"] = g_matrix
    result["gv_distance"] = gv_distance

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