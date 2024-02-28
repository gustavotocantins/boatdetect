from flask import Flask, render_template, url_for, request
from PIL import Image
import numpy as np
from pickle import load
from re import match
from glob import glob
from os import chdir
import os
import json
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/<nome>/<whatsapp>/<local>/<lider>')
def index(nome,whatsapp,local,lider):
    nome = nome.replace('%20', ' ')
    lider = lider.replace('%20', ' ')
    local = local.replace('%20', ' ')
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass

    # Obtém as credenciais do ambiente
    firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')

    # Converte as credenciais de string JSON para um dicionário
    cred_dict = json.loads(firebase_credentials)
    cred_obj = firebase_admin.credentials.Certificate(cred_dict)
    
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://assistocantinsreserva-default-rtdb.firebaseio.com/'
        })      
    # Referência para a coleção (nó) chamada 'usuarios' no caminho raiz
    ref_usuarios = db.reference(f'/')

    novo_usuario =[nome,whatsapp,local]

    ref_usuarios.child(lider).set({
    novo_usuario[1]: f'["{novo_usuario[0]}","{novo_usuario[2]}","{novo_usuario[1]}"]'
})

    return f"O {nome} foi adicionado a base de dados!"

