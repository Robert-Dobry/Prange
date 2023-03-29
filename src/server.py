from flask import Flask, render_template, request
from func import generate_matrix, gen_random_codeword, gen_random_e, add_vectors, mask_matrix, mask_vector, gen_information_set

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "MAIN PAGE"


@app.route('/gen-code', methods=["POST","GET"])
def generate():
    if request.method == "POST":
        n = int(request.form['n'])
        k = int(n/2) if (n%2==0) else int(n/2)+1

        matrix_data = generate_matrix(n,k)
        matrix={"data" : matrix_data}

        i_data = gen_information_set(n,k)
        i = {"data" : i_data}

        m_data = gen_random_codeword(matrix["data"])
        m={"data": m_data}

        e_data = gen_random_e(n,1)
        e = {"data" : e_data}

        r_data = add_vectors(m_data, e_data)
        r = {"data" : r_data}

        masked_r_data = mask_vector(r_data, i_data)
        masked_r = {"data" : masked_r_data}

        masked_matrix_data = mask_matrix(matrix_data,i_data)
        masked_matrix={"data" : masked_matrix_data}

        return render_template('matrix.html', matrix=matrix, i=i,m=m, e=e, r=r, masked_matrix=masked_matrix, masked_r=masked_r, )
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
