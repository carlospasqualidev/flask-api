import os
from keras.models import load_model

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'spotify_model.h5')

predictModel = load_model(model_path)

async def predictMusicPopularityService(dance,energy,key,speech,acoustic,instrumental,time):
    
    popularity = predictModel.predict([[dance, energy, key, speech, acoustic, instrumental, time]])

    return float(popularity[0][0])
