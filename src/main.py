import func as f

n = 5
k = int(n/2) if n%2==0 else int(n/2)+1
w = 1

print(f"Plain ISD for n={n}, k={k}, w={w}\n")

# output
error_vector = f.gen_random_e(n,w) 

# constant inputs for algorithm
gen_matrix = f.generate_matrix(n,k)
received_vector = f.add_vectors(error_vector, f.gen_random_codeword(gen_matrix))

# Print inputs and error

f.print_set(error_vector)
print('------------------')
f.print_matrix(gen_matrix)
print('------------------')
f.print_set(received_vector)
print('------------------')

# generate information set
information_set = f.gen_information_set(n,k)

# mask matrix and received vector
masked_gen_matrix = f.mask_matrix(gen_matrix,information_set)
masked_received_vector = f.mask_vector(received_vector, information_set)

# print masked vector and matrix
print('\n\n masked:')
f.print_matrix(masked_gen_matrix)
print('------------------')
f.print_set(masked_received_vector)

# invert masked matrix
inverse_masked_gen_matrix_t = f.inverse_matrix_gf2(masked_gen_matrix)
inverse_masked_gen_matrix_i = f.inverse_matrix(masked_gen_matrix)

# print inverted masked matrix
print('\n\n Inverse masked matrix:')
print('transpose:')
f.print_matrix(inverse_masked_gen_matrix_t)
print('linalg.inv:')
f.print_matrix(f.float_to_int(inverse_masked_gen_matrix_i))










