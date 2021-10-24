class Myconfig(object):
    from app import app
    import os  
    DEBUG = False
    IMG_FOLDER = os.path.join(app.root_path)+"/static/image/"
    AUDIO_FOLDER = os.path.join(app.root_path)+"/static/audio/"
    MODEL_FOLDER = os.path.join(app.root_path)+"/static/keras_model/"

    