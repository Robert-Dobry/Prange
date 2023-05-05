from flask import Flask, render_template, request, url_for, redirect, jsonify
import os, service

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "<h1>Welcome to root page. To use ISD decoder go to '/newcode' endpoint</h1>"



@app.route('/begin', methods=["POST","GET"])
def generate_code():
    if request.method == "POST":
        form = request.form
        n_size = form["n_size"]
        if n_size.isnumeric():
            os.environ["N_SIZE"] = n_size
            return redirect(url_for('calculate_gvd'))
        else:
            return "<h3>inputs must be numeric values!</h3>"
    else:
        return render_template('index.html')

@app.route('/gv-distance', methods=["POST","GET"])
def calculate_gvd():
    if request.method=='POST':
        form = request.form
        t_str = form["t_hints"]
        n_size = os.environ["N_SIZE"]
        data = service.generate_data(t_str, n_size)
        # VYRIESIT WORKFLOW SO ZADANYM T A GENEROVANIM KODU A VSTUPOV
    else:
        n_size = os.environ["N_SIZE"]
        gvd = service.gilbert_varshamov_dist(int(n_size))
        return render_template('enter_decomposition.html', gvd = gvd)
    
# @app.route('/input', methods=["POST", "GET"])
# def generate_inputs():
#     if request.method== "GET":
#         n_size = os.environ["N_SIZE"]
#         data = service.generate_data(int(n_size))
#         service.DATA = data
#         return render_template('gen_inputs.html', data=data)
#     else:
#         button = request.form["decode-button"]
#         attempts = os.environ["N_ATTEMPTS"]
#         if button == "plain":
#             output = service.decode_plain_isd(service.DATA, int(attempts))
#             return render_template('decoded.html', data=output)
#         elif button == "hints":
#             return "Under development"
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
