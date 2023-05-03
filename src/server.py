from flask import Flask, render_template, request, url_for, redirect, jsonify
import os, service

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "<h1>Welcome to root page. To use ISD decoder go to '/newcode' endpoint</h1>"


@app.route('/newcode', methods=["POST","GET"])
def generate_code():
    if request.method == "POST":
        form = request.form
        t_size = form["t_size"]
        n_attempts = form["max_attempts"]
        if t_size.isnumeric() and n_attempts.isnumeric():
            os.environ["T_SIZE"] = t_size
            os.environ["N_ATTEMPTS"] = n_attempts
            return redirect(url_for('generate_inputs'))
        else:
            return "<h3>inputs must be numeric values!</h3>"
    else:
        return render_template('index.html')
    
@app.route('/input', methods=["POST", "GET"])
def generate_inputs():
    if request.method== "GET":
        t_size = os.environ["T_SIZE"]
        data = service.generate_data(int(t_size))
        service.DATA = data
        return render_template('gen_inputs.html', data=data)
    else:
        button = request.form["decode-button"]
        attempts = os.environ["N_ATTEMPTS"]
        if button == "plain":
            output = service.decode_plain_isd(service.DATA, int(attempts))
            return render_template('decoded.html', data=output)
        elif button == "hints":
            return "Under development"
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
