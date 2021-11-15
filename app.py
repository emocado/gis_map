from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terrain')
def terrain():
    return render_template('qgis2threejs.html')

@app.route('/map')
def maps():
    return render_template('settlements.html')