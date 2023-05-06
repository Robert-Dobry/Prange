from flask import Flask, render_template, request, url_for, redirect, jsonify
import os, service

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "<h1>Welcome to root page. To use ISD decoder go to '/begin' endpoint</h1>"


@app.route('/begin', methods=["POST","GET"])
def generate_code():
    if request.method == "POST":
        form = request.form
        n_size = form["n_size"]
        n_attempts = form["n_attempts"]
        if n_size.isnumeric() and int(n_size) > 0 and (int(n_size) % 2) == 0:
            os.environ["N_SIZE"] = n_size
            os.environ["N_ATTEMPTS"] = n_attempts
            return redirect(url_for('calculate_gvd'))
        else:
            return "<h3>value n must be positive even integer</h3>"
    else:
        return render_template('index.html')


@app.route('/error-count', methods=["POST","GET"])
def calculate_gvd():
    if request.method=='POST':
        form = request.form
        t_str = form["t_hints"]
        n_size = os.environ["N_SIZE"]
        data = service.generate_data(t_str, int(n_size))
        service.DATA = data
        return redirect(url_for('generate_inputs'))
        # VYRIESIT WORKFLOW SO ZADANYM T A GENEROVANIM KODU A VSTUPOV
    else:
        n_size = os.environ["N_SIZE"]
        gvd = service.gilbert_varshamov_dist(int(n_size))
        max_errors = int((gvd-1)/2)
        return render_template('enter_decomposition.html', gvd = gvd, max_errors = max_errors)
    

@app.route('/input', methods=["POST", "GET"])
def generate_inputs():
    if request.method== "GET":
        return render_template('gen_inputs.html', data=service.DATA)
    else:
        button = request.form["decode-button"]
        attempts = os.environ["N_ATTEMPTS"]
        if button == "plain":
            print('plain')
            output = service.decode_plain_isd(service.DATA, int(attempts))
            return render_template('decoded.html', data=output)
        elif button == "hints":
            print('hints')
            output = service.decode_with_hints(service.DATA, int(attempts))
            return render_template('decoded.html', data=output)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
