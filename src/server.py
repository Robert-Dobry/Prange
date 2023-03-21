from flask import Flask, render_template, request
from func import generate_matrix, matrix_str

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "MAIN PAGE"


@app.route('/gen-code', methods=["POST","GET"])
def generate():
    if request.method == "POST":
        n = int(request.form['n'])
        k = int(request.form['k'])
        m = generate_matrix(n,k)
        return render_template('matrix.html', matrix=m)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
