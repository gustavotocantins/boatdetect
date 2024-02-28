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
    cred_obj = firebase_admin.credentials.Certificate({
  "type": "service_account",
  "project_id": "assistocantinsreserva",
  "private_key_id": "f0de950f0a9a6c1aea246917548231c230c33e18",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCTTxZIyzlkZ/WB\nu1sT0eXdiAVi21OlgIWoLE+tCkupRO4i4fDHSEpor7ySVMfv9wmcUFMeIijlr3sK\nosMXA/i9x7cYOTqLpSZE07vn5HFpmzJzCIM9T4GM+P43lXhG5cg2lb7ibXPdCpZ9\nHNwo725E+AHlz7qgl1IBpVKh/r0y2G6YJo7tefpW2IiqELG4dx//NE+5VzQ++uQz\nCMMF+1lB8Iz3G7XRkbTqBA0a3wpkdI0EgpD9QuQBs+aDCXXE13ASRW9x+wbGruom\npdpIKidZTFCTEu0HZsrAKSSSme8HMnsVVSG16bCkAD063+M8R1soS+RwZ0fDCZQv\nATMDgDGxAgMBAAECggEACoFOWTHyTYBtwqsGILthmtMeHIxVl8I68IulwZ+wAPSY\neEZdRxOXCDDYJXtZqCREPDCCQkOKCm825W2cCg0kylaZbmcjuge0sJ3aPab4ljZq\nJPKgzAOFJ/TYdEWlhoYmfrYJHy6ntPC8sKlujetylVqLusQopAExPkrNl3M03OZK\nAzuCwAkchSSBNuxH0rco23umEVqQOrndG/WLaSgXrqGsr4kYKgGh9wukXmg3kt7C\ntPj4iyYJmomPTqDtgaLaydv/0HK22iwcLJlAUbREnHvWh0WofDt0lblnxFWbsn81\n9gmodulwlyNbxB3CpKLxZ9cR31MKt6WOqofsNR117QKBgQDJESSTKx2qwQpmYhyZ\nxUQZ1GKv4SILjzpBOuCd+xEI/WrpmmcPpwiqm2v3liABurTULMtcEU6dHbdyNeAi\nVlnV3teH31vBCQv1epo/o2GEwFLuNNLsr6tAVGvPasIIDRbx3Saw2VMSKWQuoKjA\ngXbZpuKZvEJQAipEQ6qWhYabiwKBgQC7jguIkvOITMVCUbso5NlmK72VRdnRLUFP\n4qrfT+wl8RSHV6RTB80EgA8kZXlhHrGFn9g1MGQfa80HFom0R4ad8PZd72sljruj\n6cWNJzm/GBm8wlT5pdz7Ugz3gTKEP5qSFFMc0uqrz/hXAdbMthcJFeFWehsbIwhE\nSK3dKTg/MwKBgQCN6Cl2LOH9V80tQWWKKa3MxRb5pt1OZ0HoM9O/7CizvZetU6oV\nZAA72QG0diIU1l81uH+2dQiU3xpP4zJTSbqRtXtMjBnH/ciQ8nzXGUqEVPCy6llL\nbxhgiLSmaWSUJhjhjwH1owx8LvZj6kPvye/F4YDgm/v5V+3YzCEjpw2/zQKBgC70\n6T5QTFibn+dyvwEGCsfhu51b16TfR7LQdSdjwyPcr98SujlvgozV4vSh0znVjWx/\nEIqAixCy1KopomBYaAOzCHuMLa9BhQkMxkEIyRRm3Eq9/LhkJmdlq4lr91HU+sYI\nAKb+x3Isp2hhNX4bOLk1mS0ldRPeOXufFqiAYWyxAoGBALP9H0NRZZ54aCeeoksk\n2dc/BMiAaTu6E8jxdVIQcFXGkkT8r3Xyc6BpxdGehD4Ime2CwHUe4NBJDmqgIdjs\nvzS6UsRE6ke1+w/XdwSTy1NFbVhf2ZJDsTPg+UavcmIILd0KEt/y8VF/os+1V19M\nq/OZUZNCFhnKymqz/UlwEagQ\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-6aigg@assistocantinsreserva.iam.gserviceaccount.com",
  "client_id": "103763823322845760050",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6aigg%40assistocantinsreserva.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://assistocantinsreserva-default-rtdb.firebaseio.com/'
        })      
    # Referência para a coleção (nó) chamada 'usuarios' no caminho raiz
    ref_usuarios = db.reference(f'/')

    novo_usuario =[nome,whatsapp,local]

    ref_usuarios.child(lider).set({
    novo_usuario[1]: f'"["{novo_usuario[0]}","{novo_usuario[1]}","{novo_usuario[2]}"]'
})

    return f"O {nome} foi adicionado a base de dados!"

