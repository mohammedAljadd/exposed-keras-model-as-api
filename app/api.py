from app import app
from flask import request
import os
from app.utils import *


@app.route("/")
def index():

    return "Flask is working"


@app.route("/prediction", methods=["POST"])
def predict():
    
    if request.method == "POST":
            if request.files:
                image = request.files["image"]
                image_path = app.config["IMG_FOLDER"]+"/"+image.filename
                image.save(image_path)
                 
                generate_audio(image)

    return "Worked!"
