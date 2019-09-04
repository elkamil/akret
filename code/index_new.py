__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import logging
import redis
import os
import re
from logging.handlers import RotatingFileHandler
import time

import flask as fl
from flask import Response
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

from pdf2xlsx import main as pdf2xlsx
from shutdown import shutdown as shutdown_f
from variables import folder, static_dir
from create_structure import create_structure


def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')


UPLOAD_FOLDER = folder + 'pdf/'
RESULT_FOLDER = static_dir
STATIC_FOLDER = static_dir
ALLOWED_EXTENSIONS = set(['pdf', 'csv'])

app = Flask(__name__, template_folder="templates", static_folder=static_dir)
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
    path_lokale = STATIC_FOLDER + '/lokale_mieszkalne'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("Start procesu konwertowania dla pliku: " + filename)
            pdf2xlsx(filename)
            app.logger.info("Koniec procesu konwertowania dla pliku: " + filename)
            return redirect(url_for('lokale_mieszkalne'))
            # return fl.render_template('progress.html')
    return fl.render_template('lokale_mieszkalne.html', tree=make_tree(path_lokale))


@app.route("/delete", methods=['POST'])
def delete_files():
    if request.method == 'POST':
        if request.form['forwardBtn'] == 'lokale_mieszkalne':
            path = static_dir + '/lokale_mieszkalne/'
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


@app.route("/delete_history", methods=['POST'])
def delete_history_files():
    if request.method == 'POST':
        if request.form['forwardBtn'] == 'delete_history':
            path = static_dir + '/backup/lokale_mieszkalne/'
            # return_template = 'lokale_mieszkalne.html'
            return_url = 'history'

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
    path_history_lokale_m = STATIC_FOLDER + '/backup/lokale_mieszkalne'

    if request.method == 'POST':
        pass
    else:
        return fl.render_template('historia.html', tree_h_lokale=make_tree(path_history_lokale_m)[:15])
    return fl.render_template('historia.html', tree_h_lokale=make_tree(path_history_lokale_m))


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_f()
    return fl.render_template('index.html')


@app.route('/predictions')
def test():
    thePercent = str(int(40))
    print(thePercent)
    return fl.render_template("predictions.html", thePercent=thePercent)

redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(
  host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

@app.route('/progress')
def progress():
  """Get percentage progress for auto attribute process"""
  r.set("progress", str(0))
  def progress_stream():
    p = int(r.get("progress"))
    while p < 100:
      p = int(r.get("progress"))
      p_msg = "data:" + str(p) + "\n\n"
      yield p_msg
      # Client closes EventSource on 100%, gets reopened when `submit` is pressed
      if p == 100:
        r.set("progress", str(0))
      time.sleep(1)

  return Response(progress_stream(), mimetype='text/event-stream')


if __name__ == "__main__":
    handler = RotatingFileHandler(folder + '/logs/ee.log', maxBytes=10000, backupCount=1)

    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    create_structure()
    app.run(host='0.0.0.0', port=5000, debug=True)
