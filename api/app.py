from flask import Flask, render_template, url_for, request
from PIL import Image
import numpy as np
from pickle import load
from re import match
from glob import glob
from os import chdir
import os
app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pt/reconhecer', methods=['GET', 'POST'])
def reconhecer():
    if request.method == 'POST':
        # Verifica se o arquivo foi enviado
        if 'file' not in request.files:
            return 'Nenhum arquivo selecionado.'
        
        file = request.files['file']
        
        # Verifica se o usuário enviou um arquivo vazio
        if file.filename == '':
            return 'Nenhum arquivo selecionado.'
        
        return render_template('inicial.html')

    return render_template('carregamento.html')


@app.route('/pt/informacoes')
def reconhecer_en():
    return render_template('inicial.html')

if __name__ == '__main__':
    app.run()