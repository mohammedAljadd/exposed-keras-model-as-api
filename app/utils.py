import os
from gtts import gTTS
from app import app






def generate_audio(image):
    language = 'en'

    if round(get_prediction(image)[0][0]) == 1:

        audio = gTTS(
                text=f"It is you", 
                lang=language, slow=False
                )

    else:
        audio = gTTS(
                text=f"It is the calculator", 
                lang=language, slow=False
                )

    audio.save(app.config["AUDIO_FOLDER"]+"audio.mp3")
    os.system(f'start {app.config["AUDIO_FOLDER"]}audio.mp3')




def get_prediction(image):
    from keras.models import load_model
    from PIL import Image, ImageOps
    import numpy as np
    model = load_model(app.config["MODEL_FOLDER"]+'keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    return prediction
