__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from pdf2xlsx import main as pdf2xlsx
import flask as fl
import logging
from logging.handlers import RotatingFileHandler
from variables import folder, static_dir
from shutdown import shutdown as shutdown_f
import re

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
    return fl.render_template('lokale_mieszkalne.html', tree=make_tree(path_lokale))


@app.route('/lokale_uslugowe', methods=['GET', 'POST'])
def lokale_uslugowe():
    wybor = 5
    path_lokale = STATIC_FOLDER+'/lokale_uslugowe'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: "+filename)
            pdf2xlsx(filename, wybor)
            app.logger.info("Koniec procesu konwertowania dla pliku: "+filename)
            return redirect(url_for('lokale_uslugowe'))
    return fl.render_template('lokale_uslugowe.html', tree=make_tree(path_lokale))


@app.route("/grunty", methods=['GET', 'POST'])
def grunty():
    wybor = 2
    path_grunty = STATIC_FOLDER+'/grunty'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: " + filename)
            pdf2xlsx(filename, wybor)
            app.logger.info("Koniec procesu konwertowania dla pliku: " + filename)
            return redirect(url_for('grunty'))
    return fl.render_template('grunty.html', tree=make_tree(path_grunty))


@app.route("/budynki", methods=['GET', 'POST'])
def budynki():
    wybor = 3
    path_budynki = STATIC_FOLDER+'/budynki'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: "+filename)
            pdf2xlsx(filename, wybor)
            app.logger.info("Koniec procesu konwertowania dla pliku: "+filename)
            return redirect(url_for('budynki'))
    return fl.render_template('budynki.html', tree=make_tree(path_budynki))


@app.route("/mp", methods=['GET', 'POST'])
def mp():
    wybor = 4
    path_mp = STATIC_FOLDER+'/mp'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: "+filename)
            pdf2xlsx(filename, wybor)
            app.logger.info("Koniec procesu konwertowania dla pliku: "+filename)
            return redirect(url_for('mp'))
    return fl.render_template('mp.html', tree=make_tree(path_mp))


@app.route("/delete", methods=['POST'])
def delete_files():
    if request.method == 'POST':
        if request.form['forwardBtn'] == 'lokale_mieszkalne':
            path = static_dir+'/lokale_mieszkalne/'
            # return_template = 'lokale_mieszkalne.html'
            return_url = 'lokale_mieszkalne'
        elif request.form['forwardBtn'] == 'lokale_uslugowe':
            path = static_dir+'/lokale_uslugowe/'
            # return_template = 'lokale_uslugowe.html'
            return_url = 'lokale_uslugowe'
        elif request.form['forwardBtn'] == 'grunty':
            path = static_dir+'/grunty/'
            # return_template = 'grunty.html'
            return_url = 'grunty'
        elif request.form['forwardBtn'] == 'budynki':
            path = static_dir+'/budynki/'
            return_url = 'budynki'
        elif request.form['forwardBtn'] == 'mp':
            path = static_dir+'/mp/'
            return_url = 'mp'

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
    path_history_lokale_u = STATIC_FOLDER+'/backup/lokale_uslugowe'
    path_history_budynki = STATIC_FOLDER+'/backup/budynki'
    path_history_grunty = STATIC_FOLDER+'/backup/grunty'
    path_history_mp = STATIC_FOLDER+'/backup/mp'

    if request.method == 'POST':
        pass
    else:
        return fl.render_template('historia.html', tree_h_lokale=make_tree(path_history_lokale_m)[:15],
                                  tree_h_lokale_u=make_tree(path_history_lokale_u),
                                  tree_h_budynki=make_tree(path_history_budynki),
                                  tree_h_grunty=make_tree(path_history_grunty),
                                  tree_h_mp=make_tree(path_history_mp))
    return fl.render_template('historia.html', tree_h_lokale=make_tree(path_history_lokale_m),
                              tree_h_lokale_u=make_tree(path_history_lokale_u),
                              tree_h_budynki=make_tree(path_history_budynki),
                              tree_h_grunty=make_tree(path_history_grunty),
                              tree_h_mp=make_tree(path_history_mp))


@app.route('/kody_pocztowe', methods=['GET', 'POST'])
def kody_pocztowe():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: "+filename)
            app.logger.info("Koniec procesu konwertowania dla pliku: "+filename)
            return redirect(url_for('kody_pocztowe'))
    return fl.render_template('kody_pocztowe.html')

@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_f()
    return fl.render_template('index.html')


if __name__ == "__main__":
    handler = RotatingFileHandler(folder+'/logs/ee.log', maxBytes=10000, backupCount=1)
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=5000, debug=True)
