from flask import Flask, render_template, url_for, request
from PIL import Image
import numpy as np
from pickle import load
from re import match
from glob import glob
from os import chdir
import os
app = Flask(__name__)

@app.route('/')
def index():
    return "FUNCIONAAAAAAAA"

if __name__ == '__main__':
    app.run()