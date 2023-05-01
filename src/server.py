from flask import Flask, render_template, request, url_for, redirect, jsonify
import os, service

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "MAIN PAGE"


@app.route('/newcode', methods=["POST","GET"])
def generate_code():
    if request.method == "POST":
        form = request.form
        os.environ["T_SIZE"] = form["t_size"]
        return redirect(url_for('generate_inputs'))
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
        if request.form.get("name") == 'plain':
            output = service.decode_plain_isd(service.DATA)
            return render_template('decoded.html', data=output)
        else:
            print(False)
            # output = service.decode_with_hints(service.DATA)
            # return render_template('decoded.html', data=output)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
