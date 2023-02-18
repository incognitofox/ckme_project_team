from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from werkzeug.utils import secure_filename
import os
from driver import go

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/validate", methods=["GET", "POST"])
def validate():
    print(request.files)
    f = request.files['csv'] # gets the csv file from submit
    f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)))
    fname = f.filename.split(".")[0]
    print(fname)
    go(fname)
    html = pd.read_csv(f"{fname}-cleaned.csv").to_html()
    return render_template('index.html', data=html)

if __name__ == '__main__':
    app.run()
