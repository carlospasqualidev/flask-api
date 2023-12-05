from src.api.services.user.findUserByIdService import findUserByIdService
from src.api.services.musics.createMusicService import createMusicService
from src.api.services.machineLearningModels.predictMusicPopularityService import predictMusicPopularityService

async def predictMusicPopularityController(dance,energy,key,speech,acoustic,instrumental,time,name,userId):
    
    popularity = await predictMusicPopularityService(dance,energy,key,speech,acoustic,instrumental,time)

    music = await createMusicService(dance,energy,key,speech,acoustic,instrumental,time,name,popularity,userId)

    return music
    