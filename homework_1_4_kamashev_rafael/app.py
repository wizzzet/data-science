import flask
from flask import Flask, request, redirect, send_from_directory, flash
import pandas as pd
import json
import os
import numpy as np
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename

# Задаем имя серверу
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['UPLOAD_FOLDER'] = 'content/'
ALLOWED_EXTENSIONS = {'csv'}
run_with_ngrok(app)  # эта строчка не нужна, если запускаете на своем ПК


# Загрузка модели
def predict_model(x):
    return x ** 2 + 1 / x - np.log(x) * 0.5 * x ** 3


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file and file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if not file or not allowed_file(file.filename):
            flash('File not allowed')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(folder):
            os.mkdir(folder)

        file_path = os.path.join(folder, filename)
        file.save(file_path)

        with open(file_path, 'r') as f:
            df = pd.read_csv(f, header=None)
            return df.head(2).to_html()

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# Задаем функцию Predict
@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    params = flask.request.json
    if not isinstance(params, dict):
        params = flask.request.args

    if not params:
        return flask.jsonify(data)

    x = pd.DataFrame.from_dict(params, orient='index').transpose().astype(
        'int'
    ).values

    # Записываем значение prediction в data["prediction"]
    data["prediction"] = predict_model(x).tolist()
    # Записываем статус в data["success"]
    data["success"] = True

    # Возвращаем результат json format
    return flask.jsonify(data)


@app.route("/train", methods=["POST"])
def retraining():
    x = json.loads(flask.request.json)['train_x']
    y = json.loads(flask.request.json)['train_y']
    return flask.jsonify({'x': x})


# Запускаем Сервер
if __name__ == '__main__':
    app.run()
