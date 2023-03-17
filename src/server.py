from flask import Flask, render_template, request
from func import generate_matrix, matrix_str

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/gen-matrix')
def gen_matrix():
    matrix = generate_matrix(7,4)
    return matrix_str(matrix)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
