from flask import Flask, render_template, request
from func import generate_matrix, gen_random_codeword, gen_random_e, add_vectors, mask_matrix, mask_vector, gen_information_set

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "MAIN PAGE"


@app.route('/gen-code', methods=["POST","GET"])
def generate():
    if request.method == "POST":
        form = request.form
        return render_template('matrix.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
