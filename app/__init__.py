from flask import Flask, app

app = Flask(__name__)

app.config.from_object("config.Myconfig")



from app import api