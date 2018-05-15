__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import os
from flask import Flask, request, redirect, url_for, Response
from werkzeug import secure_filename
from pdf2xlsx import main as pdf2xlsx
import flask as fl
import logging
from logging.handlers import RotatingFileHandler
from variables import folder, static_dir
from shutdown import shutdown as shutdown_f
import re
import time

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')


UPLOAD_FOLDER = folder+'pdf/'
RESULT_FOLDER = static_dir
STATIC_FOLDER = static_dir
ALLOWED_EXTENSIONS = set(['pdf', 'csv'])


app = Flask(__name__, template_folder="/home/ee/code/templates", static_folder=static_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def make_tree(path):
    # lst = os.listdir(path)
    lst = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and re.match(r'.*.xlsx', f)]
    return lst


@app.route('/', methods=['GET', 'POST'])
def index():
    return fl.render_template('index.html')


@app.route('/lokale_mieszkalne', methods=['GET', 'POST'])
def lokale_mieszkalne():
    wybor = 1
    path_lokale = STATIC_FOLDER+'/lokale_mieszkalne'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: "+filename)
            pdf2xlsx(filename, wybor)
            app.logger.info("Koniec procesu konwertowania dla pliku: "+filename)
            return redirect(url_for('lokale_mieszkalne'))
            # return fl.render_template('progress.html')
    return fl.render_template('lokale_mieszkalne.html', tree=make_tree(path_lokale))






@app.route("/delete", methods=['POST'])
def delete_files():
    if request.method == 'POST':
        if request.form['forwardBtn'] == 'lokale_mieszkalne':
            path = static_dir+'/lokale_mieszkalne/'
            # return_template = 'lokale_mieszkalne.html'
            return_url = 'lokale_mieszkalne'

    app.logger.info("Start procesu usuwania plików")
    # lst = os.listdir(STATIC_FOLDER)
    # lst = os.listdir('/home/ee/ee_convert/code/static/')
    lst = os.listdir(path)
    for f in lst:
        file_path = os.path.join(path, f)
        os.remove(file_path)
    app.logger.info("Koniec procesu usuwania plików")
    return redirect(url_for(return_url))
    # return fl.render_template(return_template, tree=make_tree(path))


@app.route('/history', methods=['GET', 'POST'])
def history():
    path_history_lokale_m = STATIC_FOLDER+'/backup/lokale_mieszkalne'

    if request.method == 'POST':
        pass
    else:
        return fl.render_template('historia.html', tree_h_lokale=make_tree(path_history_lokale_m)[:15])
    return fl.render_template('historia.html', tree_h_lokale=make_tree(path_history_lokale_m))


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_f()
    return fl.render_template('index.html')


@app.route('/progress')
def progress():
    def generate():
        x = 0
        while x < 100:
            print(x)
            x = x + 10
            time.sleep(0.2)
            yield "data:" + str(x) + "\n\n"
    return Response(generate(), mimetype= 'text/event-stream')

if __name__ == "__main__":
    handler = RotatingFileHandler(folder+'/logs/ee.log', maxBytes=10000, backupCount=1)
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=5000, debug=True)
