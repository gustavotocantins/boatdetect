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
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass
    cred_obj = firebase_admin.credentials.Certificate("static/assistocantinsreserva-firebase-adminsdk-6aigg-f0de950f0a.json")
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://assistocantinsreserva-default-rtdb.firebaseio.com/'
        })      
    ref = db.reference()
    
    data = ref.get()
    return data

