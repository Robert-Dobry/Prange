from flask import Flask, render_template, request, url_for, redirect, jsonify
import os, main

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return "MAIN PAGE"


@app.route('/generate-code', methods=["POST","GET"])
def generate_code():
    if request.method == "POST":
        form = request.form
        os.environ["T_SIZE"] = form["t_size"]
        return redirect(url_for('generate_inputs'))
    else:
        return render_template('index.html')
    
@app.route('/generate-inputs', methods=["POST", "GET"])
def generate_inputs():
    if request.method== "GET":
        t_size = os.environ["T_SIZE"]
        data = main.main(int(t_size))
        return render_template('gen_inputs.html', data=data)
    else:
        return "under development"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
