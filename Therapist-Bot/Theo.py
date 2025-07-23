from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET","POST"])
def theodoreChat():
    msg = request.form['msg']
    input = msg
    return get_Theodore_response(input)

def get_Theodore_response(text):
    

