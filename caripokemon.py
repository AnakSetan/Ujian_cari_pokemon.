from flask import Flask, render_template, request, send_from_directory
import requests
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/hasil', methods=['POST'])
def result():
    if request.method=='POST':
        name=request.form['name']
        host='pokeapi.co'
        url2=f'http://{host}/api/v2/pokemon/{name}'
        datas = requests.get(url2)
        if datas.status_code==404:
            return render_template('notfound.html')
        else :
            idpoke= datas.json()['id']
            weight= datas.json()['weight']
            height= datas.json()['height']
            urlpic= datas.json()['sprites']['front_default']
        return render_template('found.html', data={'name':name, 'idpoke':idpoke,'weight':weight, 'height':height, 'urlpic':urlpic})
    else:
        return render_template('notfound.html')

@app.errorhandler(404)
def notFound(error):
    return render_template('notfound.html')

if __name__ == '__main__':
    app.run(
        debug=True
    )