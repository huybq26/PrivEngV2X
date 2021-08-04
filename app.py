import threading
import osmnx as ox
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import joblib
import time
import os
# import generate_copy
import runpy
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure

app = Flask(__name__)
# app.config['UPLOAD_EXTENSIONS'] = ['.txt']


@app.route('/input.html', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def input():
    if os.path.isfile('./static/path.jpg'):
        os.remove("./static/path.jpg")
    if os.path.isfile('./static/result.mp4'):
        os.remove("./static/result.mp4")
    if os.path.isfile('x_y_bsm_sanitized.txt'):
        os.remove("x_y_bsm_sanitized.txt")
    if os.path.isfile('x_y_bsm.txt'):
        os.remove("x_y_bsm.txt")
    if request.method == 'POST':
        raw_file = request.files['raw']
        sanitized_file = request.files['sanitized']
        if raw_file.filename != '':
            raw_file.save("x_y_bsm.txt")
        if sanitized_file.filename != '':
            sanitized_file.save("x_y_bsm_sanitized.txt")
        # file = open('generate_copy.py', 'r').read()
        if sanitized_file.filename != '' and raw_file.filename != '':
            runpy.run_path(path_name='generate_copy.py')
            runpy.run_path(path_name='generate_path.py')
            return redirect(url_for('main'))
    return render_template("input.html")


@app.route('/live.html', methods=["GET", "POST"])
@app.route('/live', methods=["GET", "POST"])
def live():
    runpy.run_path(path_name='generate_path_live.py')
    return render_template("live.html")


# @app.route("/loading.html")
# @app.route("/loading")
# # def run_script():
# #     file = open(r'generate_copy.py', 'r').read()
# #     return exec(file)
# # def loading():
# #     redirect(url_for('main'))
# #     return render_template("loading.html")
# def redirect():
#     return redirect(url_for('main'))

@app.route("/imageshow.html")
def imageShow():
    return render_template("imageshow.html")


@app.route("/main.html")
@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/login.html")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register.html")
@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/tutorial.html")
@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")


@app.route("/About.html")
@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(debug=True)
    from livereload import Server
    server = Server(app.wsgi_app)
    # server.watch('x_y_bsm_sanitized_test.txt')
    server.watch('x_y_bsm_test.txt')
    server.watch('x_y_bsm_sanitized_test.txt')
    server.serve()
