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

        imagem = Image.open(file).convert('L')  
        imagem = imagem.resize((100, 100))
        maxsize = 100,100
        imagens = []
        WIDTH, HEIGHT = imagem.size
        if WIDTH != HEIGHT:
                m_min_d = min(WIDTH, HEIGHT)
                imagem = imagem.crop((0, 0, m_min_d, m_min_d))
        imagem.thumbnail(maxsize, Image.ANTIALIAS)
        imagens.append(np.asarray(imagem))
            # Obtém o diretório do arquivo atual
        train_images = np.asarray(imagens)
        filename = url_for('static', filename='modelorede.pkl')
        #filename = './static/modelorede.pkl'
        train_images = train_images / 255
        class_names = [ 'balsa', 'canoa', 'catraia','ferry boat','iate','navio','popopo','rabeta','veleiro','voadeira']
        with open(filename, 'rb') as file:
            model = load(file)
        print(train_images.shape)
        resultado = model.predict(train_images)
        classe = np.argmax(resultado, axis = 1)

        return f"A embarcação é uma {class_names[classe[0]]} com {resultado[0][classe[0]]*100} % de precisão"
    
    return render_template('inicial.html')


@app.route('/en/reconhecer')
def reconhecer_en():
    return 'Construir aplicação aqui em Inglês'

if __name__ == '__main__':
    app.run()