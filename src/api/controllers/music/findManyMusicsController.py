from src.api.services.error.handleError import addError
from src.api.services.user.findUserByIdService import findUserByIdService
from src.api.services.musics.findManyMusicsService import findManyMusicsService

async def findManyMusicsController(id):
    
    user = await findUserByIdService(id)
    if (user is None):
        return addError("Usuário não encontrado na base de dados.") 

    musics = await findManyMusicsService(id)

    serializedMusics = []
    for music in musics:
        serializedMusics.append({
            "id": music.id,
            "name": music.name,
            "dance": music.dance,
            "energy": music.energy,
            "key": music.key,
            "speech": music.speech,
            "acoustic": music.acoustic,
            "instrumental": music.instrumental,
            "time": music.time,
            "popularity": music.popularity,
            "userId": music.userId,
            "createdAt": music.createdAt,
        })

    return serializedMusics
    